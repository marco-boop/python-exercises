string = "abcdcba"

def isPalindrome(string):
    leftPointerIndex = 0
    rightPointerIndex = len(string) - 1
    check = True
    while leftPointerIndex < rightPointerIndex:
        print("Are these two the same? ",string[leftPointerIndex]," and ",string[rightPointerIndex])
        if string[leftPointerIndex] != string[rightPointerIndex]:
            check = False
            return check
        else:
            leftPointerIndex += 1
            rightPointerIndex -= 1
    return check


answer = isPalindrome(string)
print(answer)
