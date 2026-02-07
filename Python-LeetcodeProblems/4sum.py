nums = [1,0,-1,0,-2,2]

target = 0

rs = []
n = len(nums)

nums.sort()

for i in range(n):
    
    if 0<i and nums[i] == nums[i-1]:
        continue

    for j in range(i+1, n):

        if 0<j and nums[j] ==nums[j-1]:
            continue
    
        
        l=j+1
        r =n-1

        while l<r:

            sums = nums[i] + nums[j] + nums[l] +  nums[r]


            if sums==target:
                rs.append([nums[i],nums[j],nums[l],nums[r]])

                l+=1
                r-=1

                while l<r and nums[l]==nums[l-1]:
                    l+=1
                while l<r and nums[r]==nums[r-1]:
                    r-=1
            elif sums<target:
                l+=1
            else:
                r-=1


print(rs)

