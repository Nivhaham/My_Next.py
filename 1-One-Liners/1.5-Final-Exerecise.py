import functools

with open('names', 'r') as file_names:
    # print(str(name for name in file_names.read().split() if len(name) == len(max(file_names.read().split(), key=len))))
    # 1
    print((max(file_names.read().split())))
    file_names.seek(0)
    # 2
    # length of all words in file:
    print(len(functools.reduce(lambda a, b: a + b, file_names.read().split())))
    file_names.seek(0)
    # 3 need
    print((sorted(file_names.read().split(),key=lambda e: len(e))))
    #print(file_names.read().split().sort(key=lambda e:len(e)))
    #print(min(sorted(file_names.read().split(),key=)))
    file_names.seek(0)
    #4 need to fix a bit
    with open('name_length.txt', 'w') as write_here:
        #
        print(((str([len(name) for name in file_names.read().split()]).strip('[]'))))
        write_here.write((str([len(name) for name in file_names.read().split()])))
        #

    # 5
    your_len = input("enter a length to get all the words with that length ")
    print(list(filter(lambda x: len(x) == your_len, file_names.read().split())))
