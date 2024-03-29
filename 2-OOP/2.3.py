class Pixel:

    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._blue + self._green) / 3
        self._green = avg
        self._blue = avg
        self._red = avg

    def print_pixel_info(self):
        print(f"X:{self._x}, Y:{self._y}, Color: ({self._red},{self._green},{self._blue}) ")

def main():
    my_pixel = Pixel()
    my_pixel.print_pixel_info()


if __name__ == '__main__':
    main()
