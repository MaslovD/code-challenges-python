if __name__ == '__main__':

    inputString = "(ad)+(ba)"
    tmpStack = []
    parenthesesDict = {"(": ")", ")": "("}

    for idx, val in enumerate(inputString):
        if val in parenthesesDict:
            if len(tmpStack) > 0 and tmpStack[-1] == parenthesesDict[val]:
                tmpStack.pop()
            else:
                tmpStack.append(val)
    if len(tmpStack) > 0:
        print("Parentheses aren't balanced!")
    else:
        print("Parentheses are balanced")
