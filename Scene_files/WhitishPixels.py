from PIL import Image
import urllib.request


class WhitishPixels:
    """
        An analyzer class to process images and compute pixel statistics.

        Attributes:
        image (Image): A PIL Image object to be analyzed.
        datas (list): Pixel data of the image.
        """
    def __init__(self, img_url=None, img_file=None):
        """
        Initializes an ImageAnalyzer with an image sourced from a URL or a PIL Image object.

        Parameters:
        img_url (str, optional): A URL to the image to be analyzed.
        img_file (Image, optional): A PIL Image object to be analyzed.
        """
        self.image = self._load_image(img_url, img_file)
        self.image = self.image.convert("RGB")
        self.datas = self.image.getdata()

    def _load_image(self, img_url, img_file):
        """
        Method to save the image locally if it is from the web or just reference the path given if not.
        Parameters:
        img_url (str, optional): A URL to the image to be loaded.
        img_file (Image, optional): A PIL Image object.

        Returns:
        Image: A loaded PIL Image object.

        """
        if img_url:
            urllib.request.urlretrieve(img_url, "Images/Temp/cloud_cover.png")
            return Image.open("Images/Temp/cloud_cover.png")
        elif img_file:
            return img_file
        else:
            raise ValueError("Either img_url or img_file must be provided.")

    @staticmethod
    def _is_whiteish(pixel, threshold=230): # adjust the threshold here
        """
        Static method to check if a pixel is whiteish based on the given threshold.

        Parameters:
        pixel (tuple): An RGB tuple representing a pixel.
        threshold (int): A value between 0 and 255 against which each RGB component is checked.

        Returns:
        bool: True if the pixel is whiteish, False otherwise.
        """
        r, g, b = pixel
        return r >= threshold and g >= threshold and b >= threshold

    def calculate_whiteish_pixel_percentage(self):
        """
        Calculate the percentage of whiteish pixels in the image.

        Returns:
        float: Percentage of whiteish pixels.
        """
        whiteish_pixel_count = 0
        total_pixel_count = len(self.datas)

        for pixel in self.datas:
            if self._is_whiteish(pixel):
                whiteish_pixel_count += 1

        whiteish_pixel_percentage = (whiteish_pixel_count / total_pixel_count) * 100
        return round(whiteish_pixel_percentage,2)

# Example Usage:
url = "https://genestogenomes.org/wp-content/uploads/2021/11/kakapo-crop.png"
kakapo_analyzer = WhitishPixels(img_url=url)
print(kakapo_analyzer.calculate_whiteish_pixel_percentage())
