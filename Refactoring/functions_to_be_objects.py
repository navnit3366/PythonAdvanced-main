# imagelib.py

def load_image(path):
    with open(path, "rb") as file:
        fb = file.load()
    image = img_lib.parse(fb)
    return image


def crop_image(image, width, height):
    return image


def get_image_thumbnail(image, resolution=100):
    return image


# Refactored code
class Image():
    DEFAULT_RESOLUTION = (100, 100)

    def __init__(self, path):
        self.path = path
        with open(path, "rb") as file:
            fb = file.load()
        self.image = img_lib.parse(fb)

    def get_thumbnail(self, resolution=DEFAULT_RESOLUTION):
        return self.image.resize(resolution)

    def crop_image(self, width, height):
        return self.image.resize(width, height)
