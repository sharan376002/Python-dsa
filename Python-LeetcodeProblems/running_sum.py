nums = [1,2,3,4,5]

l=0
r=1

for n in range(len(nums)):
    if r< len(nums):
        nums[r] = nums[l] + nums[r]
        l+=1
        r+=1


print(nums)
    
