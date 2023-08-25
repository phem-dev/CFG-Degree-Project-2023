# Import pygame module:
import pygame

# Import requests module:
import requests

# Import geopy.geocoders module for geolocation services:
from geopy.geocoders import Nominatim

# Import geopy.distance module to calculate distances:
from geopy.distance import geodesic

# Import math module:
import math

# Import  googletrans module for text translation:
from googletrans import Translator

# ISSTracker class:
class ISSTracker:
    def __init__(self):
        pygame.init()
        # Initialize the pygame window
        self.window_size = (800, 600)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("ISS Tracker")

        # Variables for ISS API, geolocation setup and translator:
        self.api_url = "http://api.open-notify.org/iss-now.json"
        self.geolocator = Nominatim(user_agent="iss_tracker")
        self.translator = Translator()

        # Variables to display country, altitude and speed:
        self.previous_country = ". . . loading"
        self.display_altitude = False
        self.display_speed = False

        # Load ISS and Earth images and set dimensions:
        self.iss_image = pygame.image.load("Missions/iss.png")
        self.earth_image = pygame.image.load("Missions/earth.png")
        self.earth_image_width = 300
        self.earth_image_height = 300

        # Clock and time tracking variables:
        self.clock = pygame.time.Clock()
        self.previous_time = pygame.time.get_ticks()
        self.warning_timer = pygame.time.get_ticks()

        # Button positions and dimensions:
        self.speed_button_rect = pygame.Rect(50, 200, 150, 30)
        self.altitude_button_rect = pygame.Rect(50, 300, 160, 30)
        self.power_up_button_rect = pygame.Rect(self.window_size[0] - 210, self.window_size[1] - 300, 120, 30)  # Added Power Up button
        self.power_level_text_rect = pygame.Rect(self.power_up_button_rect.left, self.power_up_button_rect.bottom - 110, 120, 30)
        self.power_level_rect = pygame.Rect(self.power_up_button_rect.left, self.power_up_button_rect.bottom + 20, 12, 12)  # Move below Power Up button
        self.exit_button_rect = pygame.Rect(350, 550, 65, 30)

        # Power level indicator squares:
        self.power_level_squares = [
            pygame.Rect(self.power_level_rect.left + i * 15, self.power_level_rect.centery - 110, 15, 15) for i in range(10)
        ]  # Creates 10 power level indicator squares

        # Power level and flag initialization:
        self.power_level = 0  # Store the current power level
        self.full_power_reached = False  # Flag to track if full power is reached

    # Method to get the current ISS location:
    def get_iss_location(self):
        response = requests.get(self.api_url)
        data = response.json()
        return float(data["iss_position"]["latitude"]), float(data["iss_position"]["longitude"])

    # Method to get the closest country to a given latitude and longitude:
    def get_closest_country(self, lat, lon):
        closest_distance = float('inf')
        closest_country = ". . . loading"

        # Reverse geocode the ISS location to find the closest country:
        locations = self.geolocator.reverse((lat, lon), exactly_one=False)
        if locations is not None:
            for location in locations:

                # Extract the country name from the raw address data:
                country = location.raw.get("address", {}).get("country", "Unknown")

                # Calculate the distance between the ISS and the location using geodesic distance:
                distance = geodesic((lat, lon), (location.latitude, location.longitude)).kilometers
                if distance < closest_distance:

                    closest_distance = distance
                    # Translate the country name to English using Google Translate
                    closest_country = self.translate_to_english(country)

        # If the closest country couldn't be determined, return the previous country name:
        if closest_country == ". . . loading":
            return self.previous_country
        else:
            # Update the previous country name and return the closest country name:
            self.previous_country = closest_country
            return closest_country

    # Translate text to English using Google Translate:
    def translate_to_english(self, text):
        try:
            translation = self.translator.translate(text, src='auto', dest='en')
            return translation.text
        except Exception as e:
            print(f"Translation error: {e}")
            return text

    # Method to Draw the ISS on the screen:
    def draw_iss(self, lat, lon, country):
        # Calculate scaling factors for latitude and longitude:
        lat_scale = self.window_size[0] / 180
        lon_scale = self.window_size[1] / 360

        # Calculate angle for ISS movement:
        angle = pygame.time.get_ticks() / 9000

        # Calculate ISS position based on angle and radius:
        radius = min(self.window_size) * 0.2
        x = int(self.window_size[0] // 2 + radius * math.cos(angle))
        y = int(self.window_size[1] // 2 + radius * math.sin(angle))

        # Clear the screen:
        self.screen.fill((0, 0, 0))

        # Draw scaled Earth image at the centre:
        earth_scaled = pygame.transform.scale(self.earth_image, (self.earth_image_width, self.earth_image_height))
        earth_centre = (self.window_size[0] // 2, self.window_size[1] // 2)
        self.screen.blit(earth_scaled, earth_scaled.get_rect(center=earth_centre))

        # Draw ISS image at calculated position:
        iss_rect = self.iss_image.get_rect(center=(x, y))
        self.screen.blit(self.iss_image, iss_rect)

        # Draw title text:
        title_font = pygame.font.Font(None, 36)
        title_text = title_font.render("International Space Station Location", True, (255, 255, 255))
        self.screen.blit(title_text, (10, 10))

        # Draw country text:
        font = pygame.font.Font(None, 36)
        text = font.render(f"Country: {country}", True, (255, 255, 255))
        self.screen.blit(text, (10, 50))

        # Draw UI buttons and power level:
        self.draw_buttons()
        self.draw_power_level()

        # Draw speed and altitude text if selected:
        font = pygame.font.Font(None, 24)
        if self.display_speed:
            speed_text = font.render("17,500 mph", True, (255, 255, 255))
            self.screen.blit(speed_text, (self.speed_button_rect.left, self.speed_button_rect.bottom + 10))
        if self.display_altitude:
            altitude_text = font.render("250 miles above Earth", True, (255, 255, 255))
            self.screen.blit(altitude_text, (self.altitude_button_rect.left, self.altitude_button_rect.bottom + 10))

        # Draw warning text if the warning timer has elapsed
        if pygame.time.get_ticks() - self.warning_timer >= 2000:
            warning_text = font.render(
                "Help! The Space Station is losing power!\nClick the power up button to restore power!",
                True, (255, 0, 0))
            warning_text_rect = warning_text.get_rect()
            warning_text_rect.center = (self.window_size[0] // 2, self.window_size[1] // 2 - 180)
            self.screen.blit(warning_text, warning_text_rect)

    # Method to draw buttons onto the screen:
    def draw_buttons(self):
        # Draw rectangles for buttons:
        pygame.draw.rect(self.screen, (30, 167, 225), self.speed_button_rect)
        pygame.draw.rect(self.screen, (30, 167, 225), self.altitude_button_rect)
        pygame.draw.rect(self.screen, (30, 167, 225), self.exit_button_rect)
        pygame.draw.rect(self.screen, (30, 167, 225), self.power_up_button_rect)

        # Set font for button labels:
        font = pygame.font.Font(None, 28)

        # Display button label texts:
        speed_button_text = font.render("Show Speed", True, (255, 255, 255))
        altitude_button_text = font.render("Show Altitude", True, (255, 255, 255))
        exit_button_text = font.render("EXIT", True, (255, 255, 255))
        power_up_button_text = font.render("Power Up", True, (255, 255, 255))

        # Display button label texts onto the screen:
        self.screen.blit(speed_button_text, (self.speed_button_rect.left + 10, self.speed_button_rect.top + 5))
        self.screen.blit(altitude_button_text, (self.altitude_button_rect.left + 10, self.altitude_button_rect.top + 5))
        self.screen.blit(exit_button_text, (self.exit_button_rect.left + 10, self.exit_button_rect.top + 5))
        self.screen.blit(power_up_button_text, (
        self.power_up_button_rect.left + 10, self.power_up_button_rect.top + 5))

    # Method to draw the power level indicator on the screen:
    def draw_power_level(self):
        font = pygame.font.Font(None, 24)

        # Display the "Current power level:" text
        power_level_text = font.render("Current power level:", True, (255, 255, 255))
        self.screen.blit(power_level_text, (self.power_level_text_rect.left, self.power_level_text_rect.top))

        # Loop through power level squares and draw them based on the current power level:
        for i, square in enumerate(self.power_level_squares):
            if i < self.power_level:
                pygame.draw.rect(self.screen, (0, 255, 0), square)  # Draw green squares
            else:
                pygame.draw.rect(self.screen, (0, 0, 0), square)  # Draw black squares
            pygame.draw.rect(self.screen, (255, 255, 255), square, 1)  # Draw white borders

        # Display "Full Power Reached!" text if the power level is >= 10:
        if self.power_level >= 10:
            full_power_text = font.render("Full Power Reached!", True, (255, 0, 0))
            self.screen.blit(full_power_text, (self.power_level_text_rect.left, self.power_level_text_rect.bottom + 20))

    # Method to increase the power level if < 10:
    def power_up_action(self):
        if self.power_level < 10:
            self.power_level += 1

    # Method to start the main program loop and handle events:
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Check if mouse button is clicked:
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.speed_button_rect.collidepoint(event.pos):
                            self.display_speed = not self.display_speed
                            self.display_altitude = False
                        elif self.altitude_button_rect.collidepoint(event.pos):
                            self.display_altitude = not self.display_altitude
                            self.display_speed = False
                        elif self.power_up_button_rect.collidepoint(event.pos):
                            self.power_up_action()
                        elif self.exit_button_rect.collidepoint(event.pos):
                            running = False

            # Get the current time in milliseconds:
            current_time = pygame.time.get_ticks()

            # Update at least every 100 milliseconds:
            if current_time - self.previous_time >= 100:
                self.previous_time = current_time

                # Get ISS location/ country info:
                iss_lat, iss_lon = self.get_iss_location()
                closest_country_name = self.get_closest_country(iss_lat, iss_lon)
                self.draw_iss(iss_lat, iss_lon, closest_country_name)

            # Frame rate set to 30 FPS:
            self.clock.tick(30)
            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    # Create an instance of the ISSTracker class and start the program
    tracker = ISSTracker()
    tracker.run()
