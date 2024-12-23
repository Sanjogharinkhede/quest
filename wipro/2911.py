def at_least_two_greater(arr):
    second_max = float('-inf')
    maxs = float('-inf')

    for i in range(len(arr)):
        if (arr[i] > maxs):
            second_max = maxs
            maxs = arr[i]
        elif (arr[i] > second_max and arr[i] < maxs):
            second_max = arr[i]

    vals=filter(lambda x:x< second_max,arr)
    print(list(vals))

at_least_two_greater([1,4,3,2,65,6,7,5])
