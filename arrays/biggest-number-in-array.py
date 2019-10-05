if __name__ == '__main__':
    inputArray = [-1, -2, -3, -6, -7, -8, 0, 100]
    maxVal = None

    if len(inputArray) > 0:

        maxVal = inputArray[0]

        for idx, val in enumerate(inputArray):
            if maxVal < val:
                maxVal = val
    print(maxVal)
