# For readme: pip install requests, pip install Pillow

# Import requests module:
import requests

# To display on screen import PIL:
from PIL import Image

# To read and store image file data:
from io import BytesIO

# Varaibles created for api data:
mars_api_key = "nFd7Ku7gaRTV7eeYliSeSsYFVOP4oN7U6J80KbFP"
rover = "curiosity"

class Mars:
    def __init__(self, challenge_name):
        self.challenge_name = challenge_name

    def greet(self):  # outputs a greeting + challenge description
        greet_string = f"Welcome to mission #3: The {self.challenge_name} mission!"
        return greet_string


# Function to check if the input is a valid number:
def is_valid(input_str):
    try:
        int(input_str)  # Try to convert the input to an integer
        return True  # If successful, return True
    except ValueError:
        return False  # If ValueError occurs, return False

while True:
    # Variable for user input choice:
    camera_choice = input("Which Mars Rover Camera Do You Want To See?\n1: Front Hazard Camera\n2: Rear Hazard Camera\n3: Navigation Camera\nPlease enter the number of the camera you want to see: ")

    # Map the player's choice to each camera:
    camera_mapping = {"1": "FHAZ", "2": "RHAZ", "3": "NAVCAM"}

    # Check if the input is a valid number
    if not is_valid(camera_choice):
        print("Invalid input. Please enter a number (1, 2, or 3).\n\n")
    else:
        camera = camera_mapping.get(camera_choice)
        if not camera:
            print("Invalid camera choice.")
        else:
            # Variable created for the Mars API URL based on the chosen camera:
            mars_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/latest_photos?camera={camera}&api_key={mars_api_key}"

            # Get response from API:
            response = requests.get(mars_url)

            # If status code is 200, get data:
            if response.status_code == 200:
                data = response.json()
                if "latest_photos" in data and data["latest_photos"]:
                    latest_img_url = data["latest_photos"][0]["img_src"]

                    # Get the image content and display it on the screen:
                    image_response = requests.get(latest_img_url)

                    # If status code is 200, display data:
                    if image_response.status_code == 200:
                        image_data = image_response.content
                        image = Image.open(BytesIO(image_data))
                        image.show()  # Display the image using the default image viewer
                    else:
                        print("Failed to fetch image. Status code:", image_response.status_code)
                else:
                    print("No latest photos available.")
            else:
                print("Failed to fetch latest Mars photo. Status code:", response.status_code)