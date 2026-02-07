height = [1,8,6,2,5,4,8,3,7]

n = len(height)-1


rs  = 1

l=0
r= len(height)-1



while l<r:
    b = abs(l - r)
    min_sum = min(height[l],height[r])
    area = b * min_sum
    rs = max(rs,area)


    if height[l] < height[r]:
        l+=1
    else:
        r-=1

print(rs)
    
    

