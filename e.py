
def sum_of_words_in_list(arr):
    s=0
    for i in arr:
        s=s+len(i)
    return s


def solution(X, Y, D):
    if(D==0): return None
    i=0
    while(Y>X):
        X+=D
        i+=1
    return i

# print(solution(3, 999111321, 7))
# 142730189

def solution2(X, Y, D):
    # Implement your solution here
    return (Y-X)//D
print(solution2(3, 999111321, 7))
