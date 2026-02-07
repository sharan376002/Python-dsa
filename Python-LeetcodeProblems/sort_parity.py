nums = [3,1,2,4]
l = 0
r = len(nums) -1

for i in range(len(nums)):
    if nums[i]%2==0:
        l+=1
    elif nums[i]%2 !=0:
       nums[r], nums[i] = nums[i],nums[r]
       r-=1

    print(nums)
