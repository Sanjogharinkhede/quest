"""
    File contains Recursion  for
    sum till number
    reverse array
    palindrome string
    GENERATE ALL SUB SEQ
    GENERATE ALL SUB SEQ with Sum=K
    GENERATE First SUB SEQ with Sum=K

    *****IMP*****
    COUNT OF SUB SEQ with Sum=K
    *****IMP*****
"""

def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
# print(sum(5))

def rev(arr):
    n=len(arr)
    for i in range(n//2):
        arr[i],arr[n-1-i]=arr[n-1-i],arr[i]
    return arr
# print(rev([1,2,4,6,4,2,1,2,8]))
# print(rev([1,2,4,6,4,2]))

def revrec(arr,n):
    if n+1==len(arr)//2:
        return arr
    arr[n],arr[len(arr)-1-n]=arr[len(arr)-1-n],arr[n]
    return revrec(arr,n-1)

# print(revrec([1,2,4,6,4,2,1,2,8],8))
# print(revrec([1,2,4,6,4,2],5))

def pal(s,n):
    if n-1<=len(s)//2:
        return True
    elif s[n]!=s[len(s)-n-1]:
        return False
    return pal(s,n-1)

# print(pal("sanjog",5))
# print(pal("naman",4))
# print(pal("xaabbcxcbbaax",12))

def generateAllSubSeq(arr,base,i):
    if len(arr)==i:
        print(base)
        return
    generateAllSubSeq(arr,base,i+1)
    base.append(arr[i])
    generateAllSubSeq(arr,base,i+1)
    base.remove(arr[i])

# generateAllSubSeq([3,2,1],[],0)


def subAllSeqWithKSum(arr,k,base,val,i):
    if len(arr)==i:
        if k==val:
             print(base)
        return
    base.append(arr[i])
    val+=arr[i]
    subAllSeqWithKSum(arr,k,base,val,i+1)
    base.remove(arr[i])
    val-=arr[i]
    subAllSeqWithKSum(arr,k,base,val,i+1)

# subAllSeqWithKSum([1,7,9,8,2,3,3,8,-1,1],9,[],0,0)

def subFirstKSum(arr,k,base,val,i,o):
    o+=1
    if len(arr)==i:
        if k==val:
            print(base,o)
            return True
        return False

    base.append(arr[i])
    val += arr[i]
    if subFirstKSum(arr, k, base, val, i + 1,o):
        return True

    base.remove(arr[i])
    val -= arr[i]
    if subFirstKSum(arr, k, base, val, i + 1,o):
        return True

    return False

print("------")
subFirstKSum([1,7,9,8,2,3,3,8,-1,1],9,[],0,0,0)

def countOfSubSeqKSum(arr,k,val,i):
    if i==len(arr):
        if k==val:
            return 1
        return 0
    val+=arr[i]
    l=countOfSubSeqKSum(arr,k,val,i+1)
    val-=arr[i]
    r=countOfSubSeqKSum(arr,k,val,i+1)
    return l+r
# print(countOfSubSeqKSum([1,7,9,8,2,3,3,8,-1,1],9,0,0))
# print(countOfSubSeqKSum([1,7,9,8,2,3,3,8],9,0,0))