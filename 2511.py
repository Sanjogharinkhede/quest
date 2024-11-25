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

q2([1,2,3,4,5,6,7,8],[22,33,44,55,66,77])