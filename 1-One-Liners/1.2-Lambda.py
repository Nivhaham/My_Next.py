import functools




def main():
    password = input("Enter Your password (integers only): ")
    lst = list(map(int, password))
    #magic= takes the first digit and adds 1 for each element in the password
    magic = functools.reduce(function, lst)
    result = (lambda x: x % 4 == 0)(magic)
    if result:
        print("Correct password!")
    else:
        print("Wrong password.")

def function(num, item):
    return num + 1




if __name__ == "__main__":
    main()
