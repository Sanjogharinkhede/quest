class Employee():
    def __init__(self , name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

class Developer(Employee):
    def __init__(self , name, age,salary,status,department):
        super().__init__(name, age, salary)
        self.status=status
        self.department=department


# obj1=Employee("ram",26,100000)
# print(obj1.__dict__)
# obj2=Developer("shyam",28,1000000,"Active","IT")
# print(obj2.name)
# print(obj2.department)


def isArmstrong(n):
    temp=n
    checkNum=0
    countDigit=len(str(n))
    while(temp>0):
        checkNum+= ((temp%10)**countDigit)
        temp//=10
    if(n==checkNum):return True
    else:return False

def isPalindrome(n):
    n=str(n)
    return n==n[::-1]

def isPalindrome2(n):
    temp=n
    newNum=0
    while(temp>0):
        newNum=newNum*10+(temp%10)
        temp//=10
    return newNum==n

# print(isArmstrong(153))
# print(isPalindrome(121))
# print(isPalindrome2(651))

def getLengthOfLetterAndDigit(string):
    digit=0
    letter=0
    for i in string:
        if(i.isdigit()):
            digit+=1
        else:
            letter+=1
    print(f"There are {letter} Letters and {digit} digit in given string")

getLengthOfLetterAndDigit(input("Enter String: "))