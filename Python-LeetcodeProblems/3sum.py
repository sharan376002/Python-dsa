nums  = [-1,0,1,2,-1,-4]

rs =[]

nums.sort()

for i,a in enumerate(nums):
    
    if 0<i and a ==nums[i-1]:
        continue

    l =i+1
    r = len(nums)-1

    while(l<r):
        sums = a+ nums[l] + nums[r]

        if sums <0:
            l+=1
        elif sums > 0:
            r-=1
        else:
            rs.append([a, nums[l], nums[r]])
            l+=1

            while nums[l] == nums[l-1] and l<r:
                l+=1

print(rs)