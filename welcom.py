# print("hello world")

# def assign1():
#     print("Provide an integer:")
#     a =input()
#     try:
#         a=int(a)
#         if a<0: return print("Please enter a positive integer")
#         return print(a*a) if a%2==0  else  print(a*a*a)
#     except:
#         print("Please provide a valid integer")
# # assign1()
#

l = [1, 2, 3, 4, 5]
search = 5


def linearSearch(arr, search):
    for i in range(len(arr)):
        if (l[i] == search):
            return i
    return -1


# print(linearSearch(l,search))
# print(linearSearch(l,3))
# print(linearSearch(l,7))

# def binarySearch(arr,num):
#     start=0
#     end=len(arr)-1
#     while start <= end:
#         mid=int(start+(end-start)/2)
#         if arr[mid]==num:
#               return mid
#         elif arr[mid]<num:
#                 start=mid+1
#         else:
#                 end=mid-1
#     return -1
# print(binarySearch(l,3))
# print(binarySearch(l,1))
# print(binarySearch(l,5))
# print(binarySearch(l,6))


def calc():
    a = int(input("enter first num: "))
    b = int(input("enter second num: "))
    c = input("enter operation to perform: ")
    match (c):
        case "+":
            print(a + b)
        case "-":
            print(a - b)
        case "*":
            print(a * b)
        case "/":
            if (b != 0):
                print(a / b)
            else:
                print("Invalid")


def calc2():
    a = int(input("enter first num: "))
    b = int(input("enter second num: "))
    c = input("enter operation to perform: ")
    if (c == "+"):
        print(a + b)
    elif (c == "-"):
        print(a - b)
    elif (c == "*"):
        print(a * b)
    elif (c == "/"):
        if (b != 0):
            print(a / b)
        else:
            print("Invalid")
    else:
        print("Invalid")


# calc2()


def logical(a):
    if (a > 90):
        print("greater then 90")
    elif (a <= 90 and a > 85):
        print("greater than 85 but less than equals to 90")
    elif (a <= 85 and a > 80):
        print("greater than 80 but less than equals to 85")
    else:
        print("less than 80")


# logical(77)
# logical(87)
# logical(99)
# logical(82)
#
def logical2():
    a = int(input("enter first num: "))
    b = int(input("enter second num: "))
    sum = a + b
    if (sum >= 80 and sum <= 85):
        print(True)
    else:
        print(False)


# logical2()
#
def logical3():
    a = int(input("enter first num: "))
    b = int(input("enter second num: "))
    mult = a * b
    if (mult == 90 or mult == 100):
        print(True)
    else:
        print(False)


# logical3()

def logical4():
    age = int(input("enter your age: "))
    gender = str(input("enter Your gender: "))
    if (gender == "M"):
        if (age > 15):
            print("male with age above 15")
        else:
            print("boy with age below 15")
    elif (gender == "F"):
        if (age > 15):
            print("Female with age above 15")
        else:
            print("girl with age less 15")
# logical4()

# for i in range(1,101):
#     print(i)
#
# i=1
# while(i<=100):
#     print(i)
#     i += 1

def revNum(n):
    rev=0
    while(n>0):
        rev=(rev*10)+(n%10)
        n=n//10
    return rev
print(revNum(1234))
print(revNum(234))
print(revNum(2034))

