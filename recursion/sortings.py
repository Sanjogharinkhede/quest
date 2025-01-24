"""
    This file contains sorting algo designed with recursion
"""

def merge_sort(arr,l,r):
    """
    The Idea is Divide  the array to 1 ele and then start merge In sorted order
    [8,7,6,7,2,4,1,2,6]
    start with dividing to half of array
    [8,7,6,7,2] [4,1,2,6]
    [8,7,6][7,2]
    [8,7][6]
    [8][7]
    now we have 1 ele array so just found if first one's ele is bigger
    if yes swap and merge else just merge
    [7,8][6]
    now again for all ele merge both array as both are sorted separately it is easy with two pointers
    [6,7,8]
    at this particular time when it get back to [8,7,6][7,2] call we will get other a
    array in sorted manner
    so might get like [6,7,8][2,7] again merge


    so we can see that we are calling two fn till they are in single ele and then we merge them

    :return:
    """
    if r<=l:
        return
    mid=(l+r)//2
    merge_sort(arr,l,mid)
    merge_sort(arr,mid+1,r)
    merge_array(arr,l,mid,r)


def merge_array(arr, l, mid, r):
    sp = []
    low = l
    right = mid + 1
    while low <= mid and right <= r:
        if arr[low] < arr[right]:
            sp.append(arr[low])
            low += 1
        else:
            sp.append(arr[right])
            right += 1
    print(f"{sp}-> (l={l},low={low})  (r={r},right={right})")
    if low > mid:
        while right < r:
            sp.append(arr[right])
            right += 1
    else:
        while low <= mid:
            sp.append(arr[low])
            low += 1

    for i in sp:
        arr[l] = i
        l += 1

# arrw=[8,7,6,7,2,4,1,2,6]
# merge_sort(arrw,0,8)
# print(arrw)


def quick_sort(arr,low,high):
    if low>=high:
        return
    pivot=partition(arr,low,high)
    quick_sort(arr,low,pivot-1)
    quick_sort(arr,pivot+1,high)

def partition(arr,low,high):
    pivot=arr[high]
    i,j=low,high
    while i<j:
        while i<=high and arr[i]<pivot:
            i+=1
        while j>low and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
        print(f"{pivot}=>", arr)
    arr[high],arr[i]=arr[i],arr[high]
    print(f"{pivot}====>", arr,i,j,low,high)

    return i

arrw2=[8,7,6,7,2,4,1,2,6]
# arrw2=[1,3,5,6,7,8]
quick_sort(arrw2,0,len(arrw2)-1)
print(arrw2)