# Import requests module:
import requests

# Import pygame module:
import pygame

# To read and store image file data:
from io import BytesIO

class MarsRoverViewer:
    def __init__(self):
        # Initialize Pygame:
        pygame.init()

        # Set up the display:
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Map the player's choice to each camera:
        self.camera_mapping = {"1": "FHAZ", "2": "RHAZ", "3": "MAST"}

        # Variables to display full camera name:
        self.camera_names = {
            "FHAZ": "Front Hazard Camera",
            "RHAZ": "Rear Hazard Camera",
            "MAST": "Navigation Camera"
        }

    # Function to check if the input is a valid number:
    def is_valid(self, input_str):
        try:
            int(input_str)  # Try to convert the input to an integer
            return True
        except ValueError:  # If ValueError occurs, return False
            return False

    def fetch_previous_images(self, camera, num_images=5):
        # Fetch previous images from the NASA Mars API:
        mars_api_key = "nFd7Ku7gaRTV7eeYliSeSsYFVOP4oN7U6J80KbFP"
        rover = "curiosity"

        # Variable created for the Mars API URL based on the chosen camera:
        mars_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?camera={camera}&api_key={mars_api_key}&sol=1000&page=1&per_page={num_images}"

        # Get response from API:
        response = requests.get(mars_url)

        # If status code is 200, get image data:
        if response.status_code == 200:
            # Parse the response data as JSON:
            data = response.json()
            if "photos" in data and data["photos"]:
                img_urls = [photo["img_src"] for photo in data["photos"]]
                images_data = []

                for img_url in img_urls:
                    # fetch image:
                    image_response = requests.get(img_url)
                    if image_response.status_code == 200:
                        image_data = image_response.content
                        images_data.append(image_data)

                # Return list of image data:
                return images_data

        return None

    def fetch_latest_image(self, camera):
        # Fetch the latest image from the NASA API
        mars_api_key = "nFd7Ku7gaRTV7eeYliSeSsYFVOP4oN7U6J80KbFP"
        rover = "curiosity"
        mars_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/latest_photos?camera={camera}&api_key={mars_api_key}"
        response = requests.get(mars_url)

        # If status code is 200, get LATEST image data:
        if response.status_code == 200:
            # Parse the response data as JSON:
            data = response.json()
            if "latest_photos" in data and data["latest_photos"]:
                latest_img_url = data["latest_photos"][0]["img_src"]
                # Fetch the latest image:
                image_response = requests.get(latest_img_url)
                if image_response.status_code == 200:
                    image_data = image_response.content

                    # Return a dictionary of data:
                    return {
                        'data': image_data,
                        'rover_name': rover.capitalize(),
                        'camera_choice_name': self.camera_names[self.camera_mapping[camera]]
                    }

        return None

    def run(self):
        running = True
        while running:
            # Variable to get user input choice:
            camera_choice = input(
                "\nWhich Mars Rover Camera Do You Want To See?\n1: Front Hazard Camera\n2: Rear Hazard Camera\n3: Navigation Camera\nPlease enter the number of the camera you want to see: "
            )

            if not self.is_valid(camera_choice):
                print("Invalid input. Please enter a number (1, 2, or 3).\n\n")
            else:
                camera = self.camera_mapping[camera_choice]
                if camera not in self.camera_mapping.values():
                    print("Invalid camera choice.")
                else:
                    # Check latest image data for camera:
                    latest_image_data = self.fetch_latest_image(camera)
                    if latest_image_data:
                        # Display latest image and camera information:
                        pygame_image = pygame.image.load(BytesIO(latest_image_data['data']))

                        # Scale the image to smaller dimensions:
                        scaled_width = 250
                        scaled_height = 250
                        pygame_image = pygame.transform.scale(pygame_image, (scaled_width, scaled_height))

                        # Display the image on the Pygame screen:
                        self.screen.fill((0, 0, 0)) # Clear screen
                        self.screen.blit(pygame_image, (100, 75))   # Display at the top-left corner

                        # Display text info/which camera: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ***CHANGE FONT******
                        font = pygame.font.Font(None, 24)
                        rover_text = font.render(f"Photo from Mars Rover {latest_image_data['rover_name']}", True,
                                                 (255, 255, 255))
                        camera_text = font.render(f"Camera: {latest_image_data['camera_choice_name']}", True,
                                                  (255, 255, 255))
                        self.screen.blit(rover_text, (100, 350))
                        self.screen.blit(camera_text, (100, 380))

                        pygame.display.flip()

                        # Loop pygame events:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                # Create running flag:
                                running = False

                    # Check if no latest image is available
                    else:
                        # Fetch and display photos from the code
                        images_data = self.fetch_previous_images(camera)
                        if images_data:
                            # Select the first image data from the list
                            selected_image_data = images_data[0]

                            # Load and scale the image:
                            pygame_image = pygame.image.load(BytesIO(selected_image_data))
                            scaled_width = 250
                            scaled_height = 250
                            pygame_image = pygame.transform.scale(pygame_image, (scaled_width, scaled_height))
                            self.screen.fill((0, 0, 0)) # CLear screen
                            self.screen.blit(pygame_image, (100, 75)) # Display at the top-left corner

                            # Display text info/which camera: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ***CHANGE FONT******
                            font = pygame.font.Font(None, 24)
                            rover_text = font.render(f"Photo from Mars Rover", True, (255, 255, 255))
                            camera_text = font.render(f"Camera: {self.camera_names[camera]}", True, (255, 255, 255))
                            self.screen.blit(rover_text, (100, 350))
                            self.screen.blit(camera_text, (100, 380))

                            pygame.display.flip()

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False
                        else:
                            # Display "No images available" message if no image found:
                            self.screen.fill((0, 0, 0))
                            font = pygame.font.Font(None, 36)
                            text = font.render("No images available.", True, (255, 255, 255))
                            self.screen.blit(text, (10, 10))
                            pygame.display.flip()

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False

        pygame.quit()


if __name__ == "__main__":
    viewer = MarsRoverViewer()
    viewer.run()