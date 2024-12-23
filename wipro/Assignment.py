

def fact(n):  # function definition so code can be modularize
    """
    Assignment 3.1:
    Factorial Function with recursion
    Time complexity: O(1)
    Space complexity: O(n)
    So best for saving Time
    """

    if n < 0:  # check whether input is correct or not
        return "Invalid"
    if n == 0 or n == 1:  # check that is number is 0 or 1 if it is break function calling and return a value
        return 1
    else:
        return n * fact(n - 1)  # say n=5  fact will be 5*4*3*2*1  so n*(n-1)*(n-2)....1





def fact2(n):  # function definition so code can be modularize
    """
    Assignment 3.1:
    Factorial Function with loop
    Time complexity: O(n)
    Space complexity: O(1)
    So best for saving Spaces
    """

    if n < 0:  # check whether input is correct or not
        return "Invalid"
    if n == 0 or n == 1:  # check that is number is 0 or 1 initially so not need for going through loop
        return 1

    factorial = 1  # initalize variable to get the factorial
    while n > 1:  # condition to end loop as if n reach 1 we will return ans
        factorial = factorial * n
        n = n - 1
    return factorial  # return calculated value of factorial





def fibonacci(n):
    """
    Assignment 3.2:
    Get the nth digit of fibonacci with recursion
    Time complexity: O(1)
    Space complexity: O(n)
    So best for saving Time

    it is a series where every number is sum of previous two number of that series
    starts with 0,1
     then 0+1=1 third num=1
     then 1+1=2 third num=2
     then 1+1=3 third num=3

    so final series will be like 0,1,1,2,3,5,8,13,21
    so to get 5th digit we can have sum if 4th digit and 3rd digit
    """

    if n < 0:  # if passed an negative number invalid status
        return "Invalid"
    if n == 0:  # if passed 0 number first digit or reached to 0 returns 1
        return 0
    elif n == 1:  # if passed 1 number second digit or reached to 1 return 2
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



def fibonacci2(n):
    """
    Assignment 3.2:
    Get the nth digit of fibonacci with
    pythonic way of swapping number
    Time complexity: O(n)
    Space complexity: O(1)
    """

    if (n < 0):
        return "Invalid"
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # pythonic way
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b  # swap numbers without third variable
    return b





def fibonacci3(n):
    """
    Assignment 3.2:
    Get the nth digit of fibonacci with
    basic way of swapping number
    Time complexity: O(n)
    Space complexity: O(1)
    """

    if (n < 0):
        return "Invalid"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a = 0
    b = 1
    c = 0  # using third variable with to swap
    while n >= 2:  # basic way to swap and sum
        c = a + b
        a = b
        b = c
        n -= 1
    return c


print(fibonacci(3))
print(fibonacci2(3))
print(fibonacci3(1999))


def assign1():
    try:
        a =int(input("Provide an integer"))
        if a<0: return print("Please enter a positive integer")
        return print(a*a) if a%2==0  else  print(a*a*a)
    except:
        print("Please provide a valid integer")


