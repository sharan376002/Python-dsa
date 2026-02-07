nums = [0,1,2,4,5,7]

l=0
rs = []

for i in range(len(nums)):

    if i+1 <len(nums) and nums[i]+1 ==nums[i+1]:
        continue

    else:
        if nums[l] == nums[i]:
            rs.append(nums[l])
        
        else:
            rs.append(str(nums[l]) + "->" + str(nums[i]))

        l = i+1
    


print(rs)

