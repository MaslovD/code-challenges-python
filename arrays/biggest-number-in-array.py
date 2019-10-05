if __name__ == '__main__':
    inputArray = [-1, -2, -3, -6, -7, -8]
    maxVal = float("-inf")

    for idx, val in enumerate(inputArray):
        if maxVal < val:
            maxVal = val
    print(maxVal)
