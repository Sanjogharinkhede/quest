"""
***************************************************************************************************
# 1. Write a code to reverse a number
***************************************************************************************************

"""


def rev(n):
    rev = 0
    while (n > 0):
        rev = rev * 10 + (n % 10)
        n //= 10
    return rev


print("----Rev----")
print(rev(1574))
print("----Rev End----")

"""
***************************************************************************************************
#2.Write code to Calculate frequency of characters in a string
***************************************************************************************************

"""


def calculate_frequency(string):
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


print("----frequency of characters----")
print(calculate_frequency("My Name Is Lakhan."))
print(calculate_frequency("WORLD WARS."))
print("----frequency of characters End----")

"""
***************************************************************************************************
#3 Write a code for bubble sort
***************************************************************************************************
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        flag = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True

        if not flag:
            break
    return arr


print("----bubble_sort----")
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
print("----bubble_sort end----")

"""
***************************************************************************************************
#4 Write code Check if the given string is Palindrome or not
***************************************************************************************************
"""


def is_palindrome(s):
    return s == s[::-1]


print("----Palindrome----")
print(is_palindrome("NAMAN"))
print(is_palindrome("RAMESH"))
print("----Palindrome End----")

"""
***************************************************************************************************
#5 Write code to Check if two strings are Anagram or not
***************************************************************************************************
"""


def is_anagram(s1, s2):
    if len(s1) != len(s2): return False
    n = len(s1)
    frequency1 = {}
    frequency2 = {}
    for i in range(n):
        frequency1[s1[i]] = frequency1.get(s1[i], 0) + 1
        frequency2[s2[i]] = frequency2.get(s2[i], 0) + 1
    return frequency2 == frequency1


print("----Anagram----")
print(is_anagram("silent", "listen"))
print(is_anagram("silen", "liste"))
print("----Anagram End----")

"""
***************************************************************************************************
#6 Write code of  Perfect number
***************************************************************************************************
"""


def perfect_num(n):
    sm = 0
    for i in range(1, n):
        if n % i == 0:
            sm += i
    return sm == n


print("----Perfect----")
print(perfect_num(6))
print(perfect_num(25))
print("----Perfect End----")



"""
***************************************************************************************************
#7 Write code of Greatest Common Divisor
***************************************************************************************************
"""
def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print("---- Greatest Common Divisor----")
print(get_gcd(36, 60))
print(get_gcd(60, 36))
print("---- Greatest Common Divisor End----")




"""
***************************************************************************************************
#8 Write the code to find the Fibonacci series upto the nth term.
***************************************************************************************************
"""

def fibonacci(n):
    if (n <= 0):
        return "Invalid"
    a, b = 0, 1
    for _ in range(1, n+1):
        print(a,end=" ")
        a, b = b, a + b
    print()

print("----Fibonacci series upto the nth term ----")
fibonacci(11)

fibonacci(7)
print("----Fibonacci series upto the nth term End----")




"""
***************************************************************************************************
#8 Merge Sort Algorithm
***************************************************************************************************
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


print("----Merge Sort ----")
print(merge_sort([123, 67, 83, -3, 99, 1182, -3]))
print(merge_sort([-3, 67, -3, -3, 99, 1182, -3]))
print("----Merge Sort End----")


