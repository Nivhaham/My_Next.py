import string


def main():
    username = "A_a1"  # input("Enter your username here: ")
    password = "A.1jk1mn0p"  # input("Enter your password here: ")

    while True:
        try:
            check_input(username, password)
        except:
            username = input("Error occurred Enter a new username here: ")
            password = input("Error occurred Enter a new  password here: ")
        else:
            print("Magic")
            break


def check_input(username, password):
    if len(username) < 3:
        print(UsernameTooShort.__str__(username))
        raise UsernameTooShort(username)
    elif len(username) > 40:
        print(UsernameTooLong.__str__(username))
        raise UsernameTooLong(username)
    elif len(password) < 8:
        print(PasswordTooShort.__str__(password))
        raise PasswordTooShort(password)

    elif len(password) > 40:
        print(PasswordTooLong.__str__(password))
        raise PasswordTooLong(password)

    for ch in username:
        if ch != '_':
            if ch.isdigit() == False:
                if ch.isalpha() == False:
                    print(UsernameContainsIllegalCharacter.__str__(username))
                    print(f"{username.index(ch)} is the index of {ch} that is illegal")
                    raise UsernameContainsIllegalCharacter(username)
    contain_small, contain_big, contain_special, contain_digit = False, False, False, False
    for ch in password:
        if ch.isupper():
            contain_big = True
        if ch.islower():
            contain_small = True
        if ch.isdigit():
            contain_digit = True
        if ch in string.punctuation:
            contain_special = True
    if contain_special == False:
        print(PasswordMissingSpecial.__str__(password))
        raise PasswordMissingSpecial(password)
    if contain_digit == False:
        print(PasswordMissingDigit.__str__(password))
        raise PasswordMissingDigit(password)
    if contain_big == False:
        print(PasswordMissingUppercase.__str__(password))
        raise PasswordMissingUppercase(password)
    if contain_small == False:
        print(PasswordMissingSpecial.__str__(password))
        raise PasswordMissingLowercase(password)
        print(PasswordMissingLowercase.__str__(password))
    else:
        print("OK")


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "Your useaname containes IllegalCharacter "

    def get_username(self):
        return self._username


class UsernameTooShort(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "Your useaname is too short "

    def get_username(self):
        return self._username


class UsernameTooLong(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "Your useaname is too long"

    def get_username(self):
        return self._username


class PasswordTooShort(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "Your password is too short"


class PasswordTooLong(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "Your password is too long"


class PasswordMissingCharacter(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "The password is missing a character"

    def get_password(self):
        return self._password


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __init__(self):
        pass

    def __str__(self):
        return "The password is missing a character (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __init__(self):
        pass

    def __str__(self):
        return "The password is missing a character (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __init__(self):
        pass

    def __str__(self):
        return "The password is missing a character (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __init__(self):
        pass

    def __str__(self):
        return "The password is missing a character (Special)"


if __name__ == '__main__':
    main()
