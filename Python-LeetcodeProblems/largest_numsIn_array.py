nums  = [1,4,5,6,7,9,11,99,3]

max_num = nums[0]

for num in nums[1:]:
    if num > max_num:
        max_num = num
print("The largest number in the array is:", max_num)