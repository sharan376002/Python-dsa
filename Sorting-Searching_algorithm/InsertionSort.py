arr = [7,1,4,5,6,7,8,5,3,9]

for i in range(1,len(arr)):
    current = arr[i]
    j = i-1
    while i>=0 and current<arr[j]:
        arr[j+1]  = arr[j]
        j-=1
    arr[j+1] = current

    # space comp[lexity- o(n)   time complexity - o(n^2)