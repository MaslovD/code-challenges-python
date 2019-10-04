if __name__ == '__main__':
    inputString="Test String Test Test Test"
    targetArray=[0 for _ in range (255)]
    for i in range(len(inputString)):
        curCharCode=ord(inputString[i])
        targetArray[curCharCode]+=1
def nonZeroFilter(number):
    if(number!=0):
        return True
    else:
        return False

for number, i in enumerate(targetArray):
    if i!=0:
        print(chr(number),i)
