n = 8

l = 0
r = n

while l <= r:
    mid = (l + r) // 2   
    
    if mid * mid == n:
        print(mid)
        break
    elif mid * mid < n:
        l = mid + 1
    else:
        r = mid - 1

else:
    print(r)   