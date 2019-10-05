from time import time


def revers_string(input_string):
    string_len = len(input_string)
    result_string = ""
    for i in range(string_len - 1, -1, -1):
        result_string += input_string[i]
    return result_string


def revers_build_in(input_string):
    return input_string[::-1]


if __name__ == '__main__':
    input_string = "test string"
    start = time()
    print(revers_string(input_string))
    elapsed_time = time() - start
    print(elapsed_time)

    input_string = "test string"
    start = time()
    print(revers_build_in(input_string))
    elapsed_time = time() - start
    print(elapsed_time)
