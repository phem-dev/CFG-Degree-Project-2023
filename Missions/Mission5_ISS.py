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
        # Initialize Pygame:
        pygame.init()

        # Set up the display:
        self.window_size = (800, 600)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("ISS Tracker")

        # Variables for ISS API, geolocation setup and translator:
        self.api_url = "http://api.open-notify.org/iss-now.json"
        self.geolocator = Nominatim(user_agent="iss_tracker")
        self.translator = Translator()

        # Variables to display country, altitude and speed:
        self.previous_country = ". . . loading"
        self.display_altitude = False  # Flag to display altitude information
        self.display_speed = False     # Flag to display speed information

        # Load ISS and Earth images
        self.iss_image = pygame.image.load("Missions/iss.png")
        self.earth_image = pygame.image.load("Missions/earth.png")

        # Set Earth image dimensions:
        self.earth_image_width = 300
        self.earth_image_height = 300

        # Clock and time tracking:
        self.clock = pygame.time.Clock()
        self.previous_time = pygame.time.get_ticks()

        # Button positions and dimensions:
        self.speed_button_rect = pygame.Rect(50, 250, 150, 30)           # Left button: speed
        self.altitude_button_rect = pygame.Rect(570, 250, 160, 30)      # Right button: altitude
        self.exit_button_rect = pygame.Rect(350, 550, 65, 30)          # Bottom button: exit

    # Get the current ISS location:
    def get_iss_location(self):
        response = requests.get(self.api_url)
        # Parse the response data as JSON:
        data = response.json()
        return float(data["iss_position"]["latitude"]), float(data["iss_position"]["longitude"])

    # Get the closest country to the ISS:
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

                # Check if this location is closer than the previously closest one:
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

    # Translate text to English using Google Translate
    def translate_to_english(self, text):
        try:
            translation = self.translator.translate(text, src='auto', dest='en')
            return translation.text
        except Exception as e:
            print(f"Translation error: {e}")
            return text

    # Draw the ISS on the screen:
    def draw_iss(self, lat, lon, country):
        # Calculate scaling factors to map latitude and longitude to screen coordinates:
        lat_scale = self.window_size[0] / 180
        lon_scale = self.window_size[1] / 360

        # Calculate the angle of rotation for the ISS movement around the Earth:
        angle = pygame.time.get_ticks() / 9000

        # Calculate the radius for the ISS circular movement path:
        radius = min(self.window_size) * 0.2
        x = int(self.window_size[0] // 2 + radius * math.cos(angle))
        y = int(self.window_size[1] // 2 + radius * math.sin(angle))

        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Scale and draw the Earth image
        earth_scaled = pygame.transform.scale(self.earth_image, (self.earth_image_width, self.earth_image_height))
        earth_center = (self.window_size[0] // 2, self.window_size[1] // 2)
        self.screen.blit(earth_scaled, earth_scaled.get_rect(center=earth_center))

        # Draw the ISS image
        iss_rect = self.iss_image.get_rect(center=(x, y))
        self.screen.blit(self.iss_image, iss_rect)

        # Draw title and country text
        title_font = pygame.font.Font(None, 36)
        title_text = title_font.render("International Space Station Location", True, (255, 255, 255))
        self.screen.blit(title_text, (10, 10))

        font = pygame.font.Font(None, 36) #-------------------------------------------------------------------------CHANGE FONT
        text = font.render(f"Country: {country}", True, (255, 255, 255))
        self.screen.blit(text, (10, 50))

        self.draw_buttons()  # Draw the buttons
        font = pygame.font.Font(None, 24)

        if self.display_speed:
            speed_text = font.render("17,500 mph", True, (255, 255, 255))
            # Display speed text just below the speed button:
            self.screen.blit(speed_text, (self.speed_button_rect.left, self.speed_button_rect.bottom + 10))

        if self.display_altitude:
            altitude_text = font.render("250 miles above Earth", True, (255, 255, 255))
            # Display altitude text just below the altitude button
            self.screen.blit(altitude_text, (self.altitude_button_rect.left, self.altitude_button_rect.bottom + 10))

    # Draw buttons on the screen
    def draw_buttons(self):
        pygame.draw.rect(self.screen, (30, 167, 225), self.speed_button_rect)         # Draw left button
        pygame.draw.rect(self.screen, (30, 167, 225), self.altitude_button_rect)      # Draw right button
        pygame.draw.rect(self.screen, (30, 167, 225), self.exit_button_rect)          # Draw bottom button

        font = pygame.font.Font(None, 28)  #-------------------------------------------------------------------------CHANGE FONT
        speed_button_text = font.render("Show Speed", True, (255, 255, 255))
        altitude_button_text = font.render("Show Altitude", True, (255, 255, 255))
        exit_button_text = font.render("EXIT", True, (255, 255,255))

        # Display button texts a little below their respective buttons
        self.screen.blit(speed_button_text, (self.speed_button_rect.left + 10, self.speed_button_rect.top + 5))
        self.screen.blit(altitude_button_text, (self.altitude_button_rect.left + 10, self.altitude_button_rect.top + 5))
        self.screen.blit(exit_button_text, (self.exit_button_rect.left + 10, self.exit_button_rect.top +5))

    # Main loop:
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
    tracker = ISSTracker()
    tracker.run()