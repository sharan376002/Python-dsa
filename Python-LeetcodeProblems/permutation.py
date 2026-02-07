"""
nums = [1,2,3]



n = len(nums)
r = n-1

num ,dem = 1,1
total_per = 0
for i in range(n):

    num *= n

    dem *= (n-r)

    total_per = num/dem

    n-=1
    r-=1

def premute(nums,total_len):
    rs = []
    l = 0
    r = len(nums)-1
    c=0
    while c<=total_len:
        if nums not in rs:
            rs.append(nums[:])
            c+=1

        nums[l],nums[l+1]= nums[l+1],nums[l]
        
        nums[l+1],nums[r] = nums[r],nums[l+1]

    
    print(rs)
            


premute(nums,total_per)
print(total_per)
"""



nums = [1,2,3]

rs=[]

def track(n):

    if n == len(nums):
        rs.append(nums[:])
        return
    
    for i in range(n, len(nums)):

        nums[n],nums[i] = nums[i],nums[n]
        track(n+1)
        nums[n],nums[i] = nums[i],nums[n]

    
track(0)
print(rs)
        
