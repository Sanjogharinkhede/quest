def q1(a,b,flag):
    if (a > 0 and b > 0): return False
    if ((a>0 or b>0) and (not flag)) or (a<0 and b<0 and flag):
        return True
    else:return False
#
# print(q1(1,-1,False)) #True
# print(q1(-182,-9121,True)) #True
# print(q1(182,9121,True)) #False

def q2(l1,l2):
    print(l1[1:4])
    l1=l1[1:4]
    print(l1)
    l3=l1+l2
    print(l3)
    del l3[2]
    print(l3)
    l3.clear()
    print(l3)

# q2([1,2,3,4,5,6,7,8],[22,33,44,55,66,77])

def q3(s1,s2):
    print(s1|s2)
    print(s1&s2)
    print(s1-s2)
    print(s1^s2)

# q3({1,3,5,7,9},{3,6,9,12})

def q4(d1):
    print(d1)
    d1[11]=17
    print(d1)
    print(d1.update({41:47}))

    print(d1.items())
    print(d1.keys())
    print(d1.values())


    print(d1.get(11))
    print(d1.pop(1))
    print(d1.popitem())
    print(d1)

# q4({1:7,11:28,21:27,31:37})

def q5():
    d1={"a":2,"b":3}
    d2={"a":6,"b":7}
    summ={}
    diff={}
    for k,y in d1.items():
       summ[k]=d1[k]+d2[k]
       diff[k]=d1[k]-d2[k]

    print(summ,diff)

# q5()

def q6():
    test_str = "Hello, Python 123!"
    test_str2 = "     Trim me    "
    test_num_str = "12345"
    test_case_str = "hello WORLD"
    print("capitalize():", test_case_str.capitalize())

    print("casefold():", test_case_str.casefold())
    print("center(30):", test_case_str.center(30))
    print("title():", test_case_str.title())
    print("swapcase():", test_case_str.swapcase())

    print("lower():", test_case_str.lower())
    print("upper():", test_case_str.upper())

    print("strip():", test_str2.strip())
    print("lstrip():", test_str2.lstrip())
    print("rstrip():", test_str2.rstrip())

    print("ljust(30):", test_case_str.ljust(30))
    print("rjust(30):", test_case_str.rjust(30))

    print("count('o'):", test_str.count('o'))
    print("format():", "My name is {} and I am {}.".format("John", 30))
    print("format_map():", "{name} is {age} years old.".format_map({'name': 'Alice', 'age': 25}))

    # print("encode():", test_str.encode())

    print("startswith('Hello'):", test_str.startswith('Hello'))
    print("endswith('123!'):", test_str.endswith('123!'))
    print("rindex('o'):", test_str.rindex('o'))
    print("rfind('o'):", test_str.rfind('o'))

    # print("expandtabs():", "Tab\texpanded".expandtabs(10))

    print("find('Python'):", test_str.find('Python'))
    print("index('Python'):", test_str.index('Python'))

    print("isalnum():", test_str.isalnum())
    print("isalpha():", test_case_str.isalpha())
    print("isascii():", test_str.isascii())
    print("isdecimal():", test_num_str.isdecimal())
    print("isdigit():", test_num_str.isdigit())
    print("islower():", test_case_str.islower())
    print("isnumeric():", test_num_str.isnumeric())
    print("isspace():", "   ".isspace())
    print("istitle():", test_case_str.istitle())
    print("isupper():", test_case_str.isupper())

    print("join(['Hello', 'World']):", ", ".join(['Hello', 'World']))


    print("maketrans():", test_str.translate(test_str.maketrans('H', 'h')))
    print("replace('Python', 'Java'):", test_str.replace('Python', 'Java'))

    print("partition('Python'):", test_str.partition('Python'))
    print("rpartition('Python'):", test_str.rpartition('Python'))

    print("split():", test_str.split())
    print("splitlines():", "Hello\nWorld".splitlines())
    print("rsplit():", test_str.rsplit())



    print("translate():", test_str.translate(test_str.maketrans("H", "h")))
    print("zfill(30):", test_num_str.zfill(7))
    print("isidentifier():", "Python".isidentifier())
    print("isprintable():", test_str.isprintable())



l=[1,2,3,4,5]
l=filter(lambda x:x%2==0,l)
print(list(l))

