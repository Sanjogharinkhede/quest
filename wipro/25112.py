lst = ["suresh", "mahesh", "deep", "kiran", "rajesh", "kumar"]

newList= filter(lambda x:len(x)>=6,lst)
print(list(newList))

ls=[[12,23,11],[89,77,56],[89,12,23]]

for i in ls:
    for j in i:
        print(j,end=" ")
    print()