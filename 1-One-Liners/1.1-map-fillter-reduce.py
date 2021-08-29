import functools
import numpy as np


# 1.1.1
def combine_coins(coin, numbers):
    print(", ".join([coin + str(num) for num in numbers]))


def squre(nums):
    l1 = [num ** 2 for num in nums]

    print(l1)


def map_squre(nums):
    print(map(squre, nums))


def t(word):
    return 't' in word


def filter_example():
    print(list(filter(t, ['abc', 't', 'tab', 'vd'])))


def secret(a, b):
    if b % 2 == 0:
        return a + b
    return a - b


def reduce_example():
    print(functools.reduce(secret, [1, 2, 3, 5, 8, 13]))


# 1.1.2
def double_letter(my_str):
    """
    :param my_str:
    :type string:
    :return: new_string
    :rtype: string
    """
    print("".join([x * 2 for x in my_str]))

# 1.1.3
def four_dividers(number):
    """

    :param number:
    :type int:
    :return: list of all the numbers that are smaller then number and make the predicate
    :rtype: list
    """
    print([x for x in range(1, number) if x % 4 == 0])

# 1.1.4
def sum_of_digits(number):
    # this is WOW
    print(functools.reduce(lambda a, b: a + b, list(map(int, str(number)))))


def main():
    combine_coins('%', [3, 4, 5, 6])
    squre([1, 2, 3, 4, 5, 6])
    map_squre([3, 4, 5, 6])
    filter_example()
    reduce_example()
    double_letter("abcd")
    four_dividers(20)
    sum_of_digits(10550)


if __name__ == "__main__":
    main()
