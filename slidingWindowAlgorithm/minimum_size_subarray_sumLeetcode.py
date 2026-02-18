nums = [2,3,1,2,4,3]
target = 7

def subsum(nums,target):
    l =0
    r= 0

    min_len = []

    subsum =0


    while r<len(nums):

        subsum += nums[r]

        while subsum >= target:
            subsum -=nums[l]
            min_len.append(r-l+1)
            l+=1
        
        r+=1
    
    return 0 if len(min_len)==0 else min(min_len)
    



p = subsum(nums,target)

print(p)