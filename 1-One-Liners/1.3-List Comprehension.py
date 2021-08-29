import functools


# 1.3.1
def intersection(list_1, list_2):
    print([x for x in list_1 for y in list_2 if x == y])


# 1.3.2
def is_prime(number):
    return any([number % i == 0 for i in range(2, number // 2 + 1)])


# 1.3.3
def is_funny(string):
    # true if string contains only 'h' and 'a'
    return all([x == 'h' or x == 'a' for x in string])


def main():
    intersection([1, 2, 3, 4], [3, 4, 5, 6])
    print(is_prime(17))
    print(is_prime(32))
    print(is_funny("asbd"))
    print(is_funny("ahahhhhaha"))

    print("##Ceaser Code decryption using one line!~!##")
    password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    print("".join([chr(ord(x)+2) for x in password]))

if __name__ == "__main__":
    main()
