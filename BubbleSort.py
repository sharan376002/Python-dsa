# bubble Sort
# time complexity n^2

# IT compare the Rwo Values and then Swaps 

arr = [1,7,8,86,98,99,343,2,4,5,65,6,12,11,13]

for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1):
        if arr[j]<arr[j+1]:
            continue

        elif arr[j]>arr[j+1]:
          #  arr[j],arr[j+1] = arr[j+1],arr[i]  # also we can do the swaping operation using a temp variabl'
            #'''
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
           # '''
print(arr)
