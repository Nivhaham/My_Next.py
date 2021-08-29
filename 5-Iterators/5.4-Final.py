def sum_of_digit(num):
    """

    :param num:
    :type int:
    :return: sums of digits
    :rtype:int
    """
    sum = 0
    list_of_digit = [char for char in (str(num))]
    for i in list_of_digit:
        sum += int(i)
    return sum


def check_id_valid(id_number):
    """

    :param id_number:
    :type id_number:
    :return: true if the id_number is valid
    :rtype: boolean
    """
    sum = 0
    list_of_digit = [char for char in (str(id_number))]
    for i in range(len(list_of_digit)):
        if (i + 1) % 2 == 0:
            temp = 2 * int(list_of_digit[i])
            temp = sum_of_digit(temp)
            sum += temp
        else:
            sum += int(list_of_digit[i])
    # return sum
    return sum % 10 == 0


class IDIterator():
    def __init__(self, _id):
        self._id = int(_id)

    def __iter__(self):
        return self

    def __next__(self):
        if self._id > 999999999:
            raise StopIteration
        if check_id_valid(self._id):
            self._id += 1
            return self._id - 1
        else:
            self._id += 1
            return ""


def id_generator(id_number):
    id_number = int(id_number)
    counter = 0
    while id_number < 999999999:
        id_number += 1
        if check_id_valid(id_number):
            counter += 1
            yield id_number
        if counter == 100:
            break


def main():
    print(check_id_valid(123456780))
    print(check_id_valid(123456782))

    your_id = input("Enter your id: ")

    type_of_action = input("Enter 'gen' or 'it' ")
    while True:
        if type_of_action=='it':
            id_iter = iter(IDIterator(your_id))
            for i in range(1000):
                curr_id = next(id_iter)
                if curr_id == "":
                    pass
                else:
                    print(curr_id)
            break
        elif type_of_action =="gen":
            gen_object = id_generator(your_id)
            for i in gen_object:
                print(i)
            break
        else:
            type_of_action = input("Enter 'gen' or 'it' ")


if __name__ == '__main__':
    main()
