if __name__ == '__main__':
    inputArray = [1, 2, 3, 4, 5, 6, 7, 3, 5, 6, 10, 1, 2, 3, 4]
    tmpDict={}
    for i in inputArray:
        if tmpDict.get(i) is not None:
            print("Array has not unique values!")
            break
        else:
            tmpDict[i]=1

    print(tmpDict)
