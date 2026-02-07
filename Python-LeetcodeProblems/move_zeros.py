
"""
nums = [0,1,0,3,12]
l = 0


for i in range(len(nums)):
    if nums[l] == 0:
        ele = nums.pop(l)
        nums.append(ele)
        l+=1


    

print(nums)
"""

nums = [0, 1, 0, 3, 12]
l = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[l] = nums[i]
        l += 1

for i in range(l, len(nums)):
    nums[i] = 0

print(nums)
