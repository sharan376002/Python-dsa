nums = [2,2,1,1,1,2,2]

for num in nums:
    count = nums.count(num)
    if count > len(nums) // 2:
        print("The majority element is:", num)
        break