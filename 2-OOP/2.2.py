class Octopus:
    def __init__(self, age=0, name="Octavio"):
        self._name = name
        self._age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


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
    # o1 = Octopus("omer", 15)
    # o2 = Octopus("niv", 25)
    # o3 = Octopus()
    # o1.birthday()
    # print(o1.get_age(), o2.get_age())
    my_pixel = Pixel()
    my_pixel.print_pixel_info()


if __name__ == '__main__':
    main()
