nums = [1,2,3,]
nums.r

n = len(nums)-1
print(n)

for i in range(len(nums)):
    if nums[i] ==9: 
        nums.append(1)
        nums.append(0)
        
    if nums[i] == nums[n]:
        nums[i]+=1
    

print(nums)
