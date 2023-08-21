import requests
from Mission_config import rejkyavic, lima, beijing, sentinel_url, headers
from Scene_files.WhitishPixels_modified import WhitishPixels


class Challenge:
    def __init__(self, challenge_name,
                 # challenge_description
                 ):
        self.challenge_name = challenge_name
        # self.challenge_description = challenge_description
        self.cities = {
            1: "Reykjavík, Iceland",
            2: "Lima, Peru",
            3: "Beijing, China"
        }
        self.city_mapping = {
            1: rejkyavic,
            2: lima,
            3: beijing
        }
        self.chosen_city = None
        self.response_message = None

    def greet(self):  # outputs a greeting + challenge description
        # return f"Welcome to the {self.challenge_name} challenge! {self.challenge_description}"
        return f"Welcome to the {self.challenge_name} challenge!"


class SatelliteImageDownloader(Challenge):

    def display_cities(self):
        cities_message = "Satellite configured to photograph the following cities:\n"
        downloading_message = "\nDownloading - please wait..."
        return cities_message, self.cities, downloading_message

    def get_image(self, city_code):

        data = self.city_mapping[city_code]
        response = requests.post(sentinel_url, headers=headers, json=data)

        if response.status_code == 200:
            with open(f"sentinel_image{city_code}.jpg", "wb") as f:  # Modify this filename in the final game if desired
                f.write(response.content)
            return f"Image successfully captured! (saved as 'sentinel_image{city_code}.jpg')"  # Edit this line for the final game
        else:
            print(response.status_code)  # Debugging only
            return "Oh no! Satellite connection failed. Please try again later."


def main():
    downloader = SatelliteImageDownloader("Satellite Imaging")
    cloud_coverage = {}  # initialise dict to store city codes and cloud coverage values
    # Initialize PyGame window and event loop

    downloader.display_cities()  # output the city names we will download images of
    for city_code in [1, 2, 3]:  # get & save all 3 city images
        print(downloader.get_image(city_code))  # remove PRINT for PyGame implementation

    for city_code in [1, 2, 3]:
        pixels = WhitishPixels(f"sentinel_image{city_code}.jpg")  # iterate through city codes, calculate whitish pixels for each
        cloud_coverage[city_code] = pixels  # write data to cloud_coverage dict
        print(cloud_coverage)



    # display image_message and update PyGame screen


if __name__ == "__main__":
    main()
