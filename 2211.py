from operator import indexOf


def fibonacci(n):
    if n < 0:
        return "Invalid"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacciSeriesTillNumber(n):
    for i in range(n):
        print(fibonacci(i), end=", " if i != n - 1 else " ")


def revString(st):
    x = ""
    for i in st:
        x = i + x
    return x


def revString2(st):
    return st[::-1]


def maxElem(arr):
    return arr[-1]  # assuming sorted array


def maxElemInUnsortedArray(arr):
    maxNum = arr[0]
    for i in range(len(arr)):
        if maxNum < arr[i]: maxNum = arr[i]
    return maxNum


# print(revString("abcd"))
# print(maxElem([1,2,3,4,5]))
# print(maxElemInUnsortedArray([11,42,73,973,-114,65]))
# fibonacciSeriesTillNumber(7)

def binarySearch(arr, num):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int(start + (end - start) / 2)
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def quest():
    arr = str(input("comma separated array: "))
    arr = arr.split(",")
    print(arr)
    return arr[3] if len(arr) > 3 else "Not Found"


# print(quest())


def longestSubstr(s):
    length = -1

    if s == "": return 0
    if len(s) == 1: return 1

    for index in range(len(s)):
        subs = ""
        newStr = s[index:len(s)]
        for inner in range(len(newStr)):
            if newStr[inner] in subs:
                break
            else:
                subs += newStr[inner]
        if length < len(subs):
            # print(subs)
            length = len(subs)
    return length


# print(longestSubstr("GEEKSFORGEEKS"))
# print(longestSubstr("pwwkew"))
# print(lengthOfLongestSubstring("AAA"))
# print(lengthOfLongestSubstring("ABC"))


# Given an array of n elements that contains
# elements from 0 to n-1,
# with any of these numbers appearing any number of times.
# Find these repeating numbers in O(n) and use only constant memory space.


def unique(arr):
    for i in range(len(arr)):
        if arr[i] in arr[i+1:]:
            print(arr[i],end=",")

def unique2(arr):
    for index in arr:
        print(index)
        if arr[index] >= 0:  # If not already marked
            arr[index] = -arr[index]  # Mark it as visited by negating the value
        # else:
            # print(index, end=", ")
# unique([1, 2, 3, 6, 3, 6, 1])
# print()
# unique([1, 2, 3, 4 ,3])

# print()
unique2([1, 2, 3, 6, 3, 6, 1])
# unique2([1, 2, 3, 4 ,3])