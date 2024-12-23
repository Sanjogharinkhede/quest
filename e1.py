# import e

lists=["abc","e","p"]

# print(e.sum_of_words_in_list(lists))


try:
    age=int(input("Enter your age"))
    s=0

    # for i in age:
    #    s= s+int(i)
    # print(s)

    # while age>0:
    #     s=s+(age%10)
    print(s)
except TypeError as e:
    print(e)

class InsufficientFund(Exception):
    def __init__(self,message):
        super().__init__(message)

def withdraw(bal,curr):
    try:
        if curr<0:
            raise Exception("Invalid amount")
        if bal>curr:
            bal-=curr
            return bal
        else:
            raise InsufficientFund("you cannot withdraw that amount")
    except InsufficientFund as e:
        print("From Insufficient Fund Exception")
        return e
    except Exception as e:
        print("From Exception")
        return e
#
# print(withdraw(1000,9999))
# print("----")
# print(withdraw(1000,-9999))
# print("----")
# print(withdraw(10000,999))
# print("----")

print(3%7)
print(10%7)



