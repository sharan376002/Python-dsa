nums = [1,2,3,4]

count = 0

diff = nums[0] + nums[1]

for i in range(len(nums)-1):

    if nums[i+1] - nums[i] !=diff:
        continue

    count+=1

print(count)
