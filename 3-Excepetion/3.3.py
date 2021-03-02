def main():
    send_invitation('avi', 15)
    send_invitation('mose', 20)


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(name, age)
    except UnderAge as under_age_error:
        print("young")
    else:
        print("You should send an invite to " + name)


class UnderAge(Exception):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        if int(self._age) < 18:
            print(f"under age {self._age} in {18 - int(self._age)} years you will be invite")
            return f"under age {self._age} in {18-int(self._age)} you will be invite"

    def get_age(self):
        return self._age

if __name__ == '__main__':
    main()