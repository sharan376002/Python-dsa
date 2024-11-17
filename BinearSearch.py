# Binear Search , n(logn)
# 704 problem in leetcode

nums = [1,43,6,7,77,4,373,9]
target = 373
l = 0
r =len(nums) -1

while l<=r:
    mid = (l+r)//2  # calculating hthe mid value 
    if  target == nums[mid]:
        print(mid, "is the index of the target element ")
        break
    elif  target > nums[mid]:
        l= mid+1 
    
    elif target < nums[mid]:
        r = mid-1