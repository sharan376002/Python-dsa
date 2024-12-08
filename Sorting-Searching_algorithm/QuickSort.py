import random

def QuickSort(arr):
    pivot = random.choice(arr)
    

    left = [i for i in arr if i<pivot]
    right = [i for i in arr if i>pivot]
    middle = [i for i in arr if i==pivot]

    return QuickSort(left)+middle+QuickSort(right)


arr = [5,3,8,9,2,1]
print(arr)

print(QuickSort(arr))
print(arr)
