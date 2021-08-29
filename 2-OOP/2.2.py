class Octopus:
    def __init__(self, age=0, name="Octavio"):
        self._name = name
        self._age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age




def main():
    o1 = Octopus("omer", 15)
    o2 = Octopus("niv", 25)
    o3 = Octopus()
    o1.birthday()
    print(o1.get_age(), o2.get_age())

    my_pixel = Pixel()
    my_pixel.print_pixel_info()


if __name__ == '__main__':
    main()
