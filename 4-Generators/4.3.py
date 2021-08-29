# Generator function

def get_fibo():
    x, y = 0, 1
    yield x
    yield y
    while True:
        yield x+y
        temp=x
        x=y
        y+=temp

def main():
    instance = get_fibo()
    print(next(instance))
    print(next(instance))
    print(next(instance))
    print(next(instance))
    print(next(instance))
    print(next(instance))
    print(next(instance))
    print(next(instance))
    print(next(instance))
    print(next(instance))


if __name__ == '__main__':
    main()
