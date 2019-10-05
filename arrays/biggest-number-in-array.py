def max_number_in_array_v2(input_array):
    return max(input_array)


def max_number_in_array(input_array):
    max_val = float("-inf")

    for idx, val in enumerate(input_array):
        if max_val < val:
            max_val = val
    return max_val


if __name__ == '__main__':
    input_array = [-1, -2, -3, -6, -7, -8]

    print(max_number_in_array(input_array))
    print(max_number_in_array_v2(input_array))
