class Animal:
    zoo_name = "Hayaton"

    def __init__(self, _name, _hunger=0):
        self._name = _name
        self._hunger = _hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hunger > 0

    def feed(self):
        self._hunger -= 1

    def __str__(self):
        return self.get_name()

    def talk(self):
        pass


class Dog(Animal):
    def __init__(self, name, hunger):
        super().__init__(name, hunger)

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def __init__(self, _name, _hunger=0):
        super().__init__(_name, _hunger)

    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, _name, _hunger=0, _stink_count=6):
        super().__init__(_name, _hunger)
        self._stink_count = _stink_count

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    def __init__(self, _name, _hunger=0):
        super().__init__(_name, _hunger)

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):
    def __init__(self, _name, _hunger=0, _color="Green"):
        super().__init__(_name, _hunger)
        self._color = _color

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    brownie = Dog("Brownie", 10)
    zelda = Cat("Zelda", 3)
    stinky = Skunk("Stinky")
    keith = Unicorn("Keith", 7)
    lizzy = Dragon("Lizzy", 5)

    zoo_lst = []
    zoo_lst.append(brownie), zoo_lst.append(zelda), zoo_lst.append(stinky), zoo_lst.append(keith), zoo_lst.append(lizzy)
    for animel in zoo_lst:
        if animel.is_hungry():
            print(type(animel), animel.get_name())
        while animel.is_hungry():
            animel.feed()
            animel.talk()
            if isinstance(animel, Dog):
                animel.fetch_stick()
            if isinstance(animel, Cat):
                animel.chase_laser()
            if isinstance(animel, Skunk):
                animel.stink()
            if isinstance(animel, Unicorn):
                animel.sing()
            if isinstance(animel, Dragon):
                animel.breath_fire()


if __name__ == '__main__':
    main()
