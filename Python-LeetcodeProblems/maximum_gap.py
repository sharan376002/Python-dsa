nums = [3,6,9,1]

if len(nums)<=2:
    print(0)

nums.sort()

sums =0
l=0
r=1
while r<len(nums):
    cur =nums[r] - nums[l]
    if  sums<cur:
        sums = cur
    
    l+=1
    r+=1

print(sums)

