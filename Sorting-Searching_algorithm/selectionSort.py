
# selection Sort
# we select the minimun minimum number to sort the array

arr = [2,12,5,6,7,8,1,5]

for pos in range(len(arr)-1):
    min = pos
    for i in range(pos+1,len(arr)):
        if arr[i]<arr[min]:
            min = i
    arr[min],arr[pos] = arr[pos],arr[min]


print(arr)