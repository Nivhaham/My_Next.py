# Poli And Inheritence
class BigThing:
    def __init__(self, something):
        self._something = something

    def size(self):
        if type(self._something) is int:
            return self._something
        if type(self._something) is list or dict or str:
            return len(self._something)


class BigCat(BigThing):
    def __init__(self, something, weight):
        super().__init__(something)
        self._weight = weight
<<<<<<< HEAD
    def size(self):
        if self._weight>15 and self._weight <=20:
=======

    def size(self):
        if self._weight > 15 and self._weight <= 20:
>>>>>>> master
            print("Fat")
        if self._weight > 20:
            print("Very Fat")
        else:
            print("OK")
<<<<<<< HEAD
=======


>>>>>>> master
def main():
    cutie = BigCat("mitzy", 22)
    cutie.size()


if __name__ == '__main__':
    main()
