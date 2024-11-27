# Hackerrank Copy  Mostly Questions are  from leetcode so solved there to get better testcases
# Copied here




def minDistance(ls, w1, w2):
    """Given a list of words followed by two words, the task is to find the minimum
     distance between the given two words in the list of words.
    """
    mi = 9999999999
    ind1 = ind2 = -1
    for i in range(len(ls)):
        if (ls[i] == w1):
            ind1 = i
        elif (ls[i] == w2):
            ind2 = i
        if (ind1 != -1 and ind2 != -1 and mi > abs(ind1 - ind2)):
            mi = abs(ind1 - ind2)
    return mi if mi != 9999999999 else "Not Found"


print(minDistance(["the", "quick", "brown", "fox", "quick"], "the", "fox"))
print(minDistance(["geeks", "for", "geeks", "contribute", "practice"], "geeks", "practice"))
print(minDistance(["geeks", "for", "geeks", "contribute", "practice"], "geeks", "practic"))


def q1Copy():
    """
    Given the participants' score sheet for your University Sports Day,
    you are required to find the runner-up score.
    You are given  scores. Store them in a list and find the score of the runner-up.
    """
    n = int(input())
    arr = map(int, input().split())
    mi = -9999999
    secondMax = -9999999

    for i in arr:
        if (i > mi):
            secondMax = mi
            mi = i
        elif (i > secondMax and i < mi):
            secondMax = i
    print(secondMax)


def q2Copy():
    """
    Let's learn about list comprehensions!
     You are given three integers  and  representing the dimensions of a cuboid along with an integer .
      Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to .
      Here, use list comprehensions rather than multiple loops, as a learning exercise.
    """
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    ls = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k != n)]
    print(ls)


def q3Copy():
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))


def q4Copy():
    from math import degrees, atan2

    AB = float(input())
    BC = float(input())

    MBC = round(degrees(atan2(AB, BC)))
    print((str(MBC)), chr(176), sep='')


# q4Copy()

def q5Copy():
    """
    Word Order
    """
    n = int(input())
    dt = {}
    for i in range(n):
        x = input()
        dt[x] = dt.get(x, 0) + 1
    print(len(dt))
    for i in dt:
        print(dt[i], end=" ")


def q6Copy():
    """
    No Idea!
    """
    n, m = input().split(" ")
    vals = input().split(" ")
    a = set(input().split(" "))
    b = set(input().split(" "))

    happiness = 0

    for val in vals:
        if (val in a): happiness += 1
        if (val in b): happiness -= 1

    print(happiness)


def q7Copy():
    """
    Nested Lists
    """
    dt = {}
    mi = 101
    sec = 101
    for _ in range(int(input())):
        name = input()
        score = float(input())

        if (score in dt):
            dt[score].append(name)
        else:
            dt[score] = [name]

        if (score < mi):
            sec = mi
            mi = score
        elif (score < sec and score > mi):
            sec = score
    # print(dt)
    sortedName = sorted(dt[sec])
    for i in sortedName:
        print(i)


def q8Copy():
    """
    Find the percentage
    """
    from functools import reduce
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    ls = student_marks[query_name]
    sm = reduce(lambda a, b: a + b, ls)
    # print(round(sm/len(ls), 2))
    print(f"{sm / len(ls):.2f}")

q8Copy()

def mutate_string(string, position, character):
    """
    Mutation
    :param string:
    :param position:
    :param character:
    :return:
    """
    return string[:position] + character + string[position+1:]


# !/bin/python3




def time_delta(t1, t2):
    from datetime import datetime
    """
    Time Delta
    :param t1:
    :param t2:
    :return:
    """
    dt = "%a %d %b %Y %H:%M:%S %z"
    diff = datetime.strptime(t1, dt) - datetime.strptime(t2, dt)
    return str(abs(int(diff.total_seconds())))

def merge_the_tools(string, k):
    """
    Merge the Tools
    :param string:
    :param k:
    :return:
    """
    for i in range(0,len(string),k):
        st=string[i:i+k]
        # newSt=""
        # for j in st:
        #     if(j not in newSt):
        #         newSt+=j
        chars=set()
        newStList=[char for char in st if char not in chars and not chars.add(char)]
        print("".join(newStList))

def List_comp():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    ls = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k != n)]
    print(ls)

def q13Copy():
        n = int(input())
        arr = map(int, input().split())

        mi = -9999999
        secondMax = -9999999

        for i in arr:
            if (i > mi):
                secondMax = mi
                mi = i
            elif (i > secondMax and i < mi):
                secondMax = i
        print(secondMax)
