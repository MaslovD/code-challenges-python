def calculate_max_binary_gap(N):
    bin_representation = format(N, '08b')
    print(bin_representation)
    counter = 0
    for i, val in enumerate(bin_representation):
        if val == '0':
            counter += 1
        else:
            if i < len(bin_representation): counter = 0

    return counter


def calculate_max_binary_gap_v2(N):
    print("print(format(N, 'b'))")
    print(format(N, 'b'))

    print("format(N, 'b').strip('0')")
    print(format(N, 'b').strip('0'))

    print("format(N, 'b').strip('b').split('1')")
    print(format(N, 'b').strip('b').split('1'))

    return len(max(format(N, 'b').strip('0').split('1')))


if __name__ == '__main__':
    print(calculate_max_binary_gap_v2(1041))
