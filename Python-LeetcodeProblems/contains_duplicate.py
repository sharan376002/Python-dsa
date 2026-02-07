nums = [1,1,3,4,9]

#hashset = set()
i=1
while i<len(nums):
     
     if nums[i] == nums[i -1]:
            nums.pop(i)
            nums.pop(i -1)

     else:
        i+=1
    

print(nums)  