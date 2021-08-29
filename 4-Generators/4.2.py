# the function takes "1-2,4-4,8-10" returns this  [1, 2, 4, 8, 9, 10]

import re


def parse_ranges(ranges_string):
    parse_data = re.split(',|-', ranges_string)

    first_gen = (list_of_num for list_of_num in parse_data)
    l = []
    while True:
        try:
            postproc = [next(first_gen), next(first_gen)]
            # print(list(first_gen))
            second_gen = (x for x in range(int(postproc[0]), int(postproc[1]) + 1))
            while True:
                try:
                    # print(next(second_gen))
                    l.append(next(second_gen))
                    # print(list(second_gen))
                except:
                    break
        except:
            break
    print(l)
    #return (n for n in l)


def main():
    parse_ranges("1-2,4-4,8-10")


if __name__ == '__main__':
    main()
