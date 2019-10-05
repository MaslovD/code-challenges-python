def do_sort(data):
    array_size = len(data)
    for i in range(array_size):
        for idx in range(array_size - i - 1):
            cur_val = data[idx]
            next_val = data[idx + 1]

            if idx != array_size and next_val < cur_val:
                data[idx] = next_val
                data[idx + 1] = cur_val

    return data


if __name__ == '__main__':
    inputArray = [1, 2, 3, 100, 9, 4, 5, 3, 2, 3, 4]
    print(do_sort(inputArray))
