import requests
from Missions.Mission_config import rejkyavic, lima, beijing, sentinel_url, headers
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
        """Outputs the cities in a readable way

        Returns: cities_message, city codes + names, downloading_message

        """
        cities_message = "Satellite configured to photograph the following cities:|"
        downloading_message = "|Downloading - please wait..."
        formatted_cities = [f"{key}: {value}" for key, value in self.cities.items()]
        return cities_message, ("|".join(formatted_cities)), downloading_message

    def get_image(self):
        """ Iterates through the cities in city_mapping, calls API, saves each image as a temp file
        Returns: confirmation message for each image saved OR error message if API connection error
        """
        for city_code in [1, 2, 3]:  # for the 3 hardcoded cities
            data = self.city_mapping[city_code]
            response = requests.post(sentinel_url, headers=headers, json=data)

            if response.status_code == 200:
                # Currently saving images as local files - think we want to change this to pygame objects?
                with open(f"sentinel_image{city_code}.jpg", "wb") as f:  # Modify filename in the final game if desired
                    f.write(response.content)
                print(f"Image {city_code} successfully captured!")  #saves as "sentinel_imageX.jpg
                #return f"Image {city_code} successfully captured!"

            else:
                print(response.status_code)  # Debugging only - remove
                print("Oh no! Satellite connection failed. Please try again later.")  # remove for PG
                #return "Oh no! Satellite connection failed. Please try again later."

        # ALSO NEED TO display the 3 saved images to the user (PyGame). these should either be clickable or have
        # corresponding buttons below them for user to select the cloudiest photo image

    def whitish_pixels(self):
        """Uses whitish_pixels function to calculate cloud coverage based on how many whitish pixels are detected in
        each photo.
        Returns: cloud_coverage dictionary of city codes and cloud coverages

        """
        cloud_coverage = {}  # initialise new dict to store city codes and cloud coverage values

        for city_code in [1, 2, 3]:
            #pixels = WhitishPixels(img_file=f"sentinel_image{city_code}.jpg")  # iterate through city codes, calculate
            # whitish pixels for each
            # NEEDS CHANGING if using pygame objects to render images (current code uses jpg files)
            pixels = WhitishPixels(img_file=f"C:\\Users\Rea\PycharmProjects\Group-6-Thales-Gals\Missions\sentinel_image{city_code}.jpg")
            cloud_coverage[city_code] = pixels  # write data to cloud_coverage dict
        print(cloud_coverage)  # debugging only, Return for PyGame

        self.player_enter_cloudiest_city(cloud_coverage)


    def player_enter_cloudiest_city(self, cloud_coverage):
        # logic here for capturing player input. Ask player to enter the key for the cloudiest city
        # if key entered = key of city with most cloud cover, mission successful

        pass


def main():
    downloader = SatelliteImageDownloader("Satellite Imaging")  # initialise a class object
    print(downloader.display_cities())  # output the city names we will download images of ---- RETURN FOR PG
    print(downloader.get_image())  # fetch & save images for the 3 x cities ---- RETURN FOR PG
    print(downloader.whitish_pixels())  # call whitish_pixels function to analyse cloud coverage ---- RETURN FOR PG

    # Initialize PyGame window and event loop


    # display image_message and update PyGame screen


if __name__ == "__main__":
    main()
