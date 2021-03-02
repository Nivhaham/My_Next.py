import functools


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


def main():
    combine_coins('%', [3, 4, 5, 6])
    squre([1, 2, 3, 4, 5, 6])
    map_squre([3, 4, 5, 6])
    filter_example()
    reduce_example()


if __name__ == "__main__":
    main()
