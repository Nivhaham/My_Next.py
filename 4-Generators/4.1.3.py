import sys
import math

# 4.1.3
def first_prime_over(n):
    first_prime = (i for i in range(n + 1, sys.maxsize) if is_prime(i))
    print(next(first_prime))

def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


# enter a number that you want the first prime after this number
def main():
    first_prime_over(54734682)


if __name__ == '__main__':
    main()
