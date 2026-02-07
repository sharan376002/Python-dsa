numbers = [2,7,11,15]
target = 9


l = 0
r = len(numbers)-1

while l<r:

    sums = numbers[l] + numbers[r]

    if sums==target:
        print(l,r)
    elif sums < target:
        l+=1
    else:
        r-=1
