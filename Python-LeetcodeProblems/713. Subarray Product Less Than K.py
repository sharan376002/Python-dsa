nums = [10,5,2,6]
k = 100


sub_count = 0
sums = 1

l=0

for r in range(len(nums)):

    sums *=nums[r]
    if nums[r] <k:
        sub_count +=1
    if sums <k:
        sub_count +=1   
    
    while l<r and  sums >=k:
        sums -=nums[l]

        l+=1

    
print(sub_count)


