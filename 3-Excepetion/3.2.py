import os
def read_file(file_name):
    print("__CONTENT_START__")
    try:
        with open(file_name, 'r') as file:
            print(file.read())

    except:
        print("__NO_SUCH_FILE__")

    finally:
        print("__CONTENT_END__")


def main():
    print(os.getcwd()+"\\names")
    read_file(os.getcwd()+"\\names")


if __name__ == '__main__':
    main()
