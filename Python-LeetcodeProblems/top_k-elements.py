nums = [1,2,1,2,1,2,3,1,3,2 ]
k = 2

l = 0
r =1
rs =set()

for i in range(len(nums)):
    
    if nums[l]==nums[r]:
        l+=1
        r+=1
    else:
        if nums[i]not in rs:
            rs.add(nums[l])
            rs.add(nums[r])


print(list(rs))