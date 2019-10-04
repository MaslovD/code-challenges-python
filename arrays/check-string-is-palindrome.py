def is_palindrome(inputString):
    for i, char in enumerate(inputString):
        if inputString[i] != inputString[-1-i]:
            return False
    return True

if __name__ == '__main__':

    inputString = "annaD"
    if is_palindrome(inputString):
        print("String is palindrome")
    else:
        print("String is not palindrome")
