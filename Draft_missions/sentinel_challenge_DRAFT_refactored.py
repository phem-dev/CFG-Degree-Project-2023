import requests
from stratobus_challenges_config import rejkyavic, lima, beijing, sentinel_url, headers


class SatelliteImageDownloader:
    def __init__(self):
        self.cities = {
            1: "Reykjavík, Iceland",
            2: "Lima, Peru",
            3: "Beijing, China"
        }

        self.chosen_city = None
        self.response_message = None

    def display_city_options(self):
        return self.cities

    def choose_city(self, city_choice):
        if city_choice in self.cities:
            self.chosen_city = city_choice
            return "City chosen: " + self.cities[city_choice]
        else:
            return "Invalid city choice"

    def get_image(self):
        if self.chosen_city is None:
            return "Please choose a city first."

        data = None
        if self.chosen_city == 1:
            data = rejkyavic
        elif self.chosen_city == 2:
            data = lima
        elif self.chosen_city == 3:
            data = beijing

        response = requests.post(sentinel_url, headers=headers, json=data)

        if response.status_code == 200:
            with open("sentinel_image.jpg", "wb") as f:  # Modify this line in the final game if desired
                f.write(response.content)
            return "Image successfully captured! (saved as 'sentinel_image.jpg')"  # Edit this line for the final game
        else:
            print(response.status_code)  # Debugging only
            return "Oh no! Satellite connection failed. Please try again later."


# In your PyGame setup, you would use an instance of SatelliteImageDownloader
def main():
    downloader = SatelliteImageDownloader()

    # Initialize PyGame window and event loop

    while True:
        # Display city options and capture player input
        city_options = downloader.display_city_options()
        # Capture player input using your PyGame event handling logic

        # replace this with actual event handling
        player_input_event = None
        if player_input_event:
            player_input = player_input_event  # replace with the actual player input

            if int(player_input) in [1, 2, 3]:  # may need to convert data type depending on how PyGame handles text inp
                response_message = downloader.choose_city(player_input)  # get photo of the chosen city
                # display response_message and update PyGame screen

        # download and display the satellite image
        if response_message and "City chosen" in response_message:
            image_message = downloader.get_image()
            # display image_message and update PyGame screen


if __name__ == "__main__":
    main()
