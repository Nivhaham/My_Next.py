import functools

<<<<<<< HEAD
def main():
    #a = lambda x: x
    #print(a(3))
    password = input("Enter Your password (integers only): ")
    lst = list(map(int, password))
    #magic= adding 1 (times list len's -1) for the first digits
=======



def main():
    password = input("Enter Your password (integers only): ")
    lst = list(map(int, password))
    #magic= takes the first digit and adds 1 for each element in the password
>>>>>>> master
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
