from PIL import Image
import urllib.request


class WhitishPixels:
    """
        An analyser class to process images and compute pixel statistics.

        Attributes:
        image (Image): A PIL Image object to be analyzed.
        datas (list): Pixel data of the image.
        """
    def __init__(self, img_file):
        """
        Initializes an ImageAnalyzer with an image sourced from a URL or a PIL Image object.

        Parameters:
        img_url (str, optional): A URL to the image to be analyzed.
        img_file (Image, optional): A PIL Image object to be analyzed.
        """
        self.image = self._load_image(img_file)
        self.image = self.image.convert("RGB")
        self.datas = self.image.getdata()

    def _load_image(self, img_file):
        """
        Method to reference the image path.
        Parameters:
        img_file (Image, optional): A PIL Image object.

        Returns:
        Image: A loaded PIL Image object.

        """
        if isinstance(img_file, str):  # Check if img_file is a string (file path)
            return Image.open(img_file)  # Open the image using PIL
        elif isinstance(img_file, Image.Image):  # Check if img_file is already a PIL.Image object
            return img_file
        else:
            raise ValueError("Hmm, no image found! Please try again...")

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
        whitish_pixel_count = 0
        total_pixel_count = len(self.datas)

        for pixel in self.datas:
            if self._is_whiteish(pixel):
                whitish_pixel_count += 1

        whitish_pixel_percentage = (whitish_pixel_count / total_pixel_count) * 100
        return round(whitish_pixel_percentage,2)


def main():  # do we need img_file here?? causes conflict below if we dont have it, not sure
    image_to_analyse = "sentinel_image1.jpg"  # cant work out how to make this work for accepting the img_file from satellite_images_v2 file (rather than hardcoding)
    analyzer = WhitishPixels(image_to_analyse)
    result = analyzer.calculate_whiteish_pixel_percentage()
    return result


if __name__ == "__main__":
    main()
