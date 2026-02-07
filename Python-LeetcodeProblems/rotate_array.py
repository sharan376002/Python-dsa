nums = [1,2,3,4,5,6,7]
k = 3

n= len(nums)    

# actual formula is (i+k)% len(nums)
k = k%n

n = len(nums)
k = k%n

l = 0
r = len(nums)-1

while l<r:
    nums[l], nums[r] = nums[r], nums[l]       # reverse the total array
    l+=1
    r-=1

l,r = 0,k-1
while l<r:
    nums[l],nums[r] =nums[r],nums[l]         # again reverse the k part only 
    l+=1
    r-=1

l,r = k,len(nums)-1
while l<r:
    nums[l],nums[r] = nums[r],nums[l]    # agin reverse the next part then it totaly get rotated
    l+=1
    r-=1