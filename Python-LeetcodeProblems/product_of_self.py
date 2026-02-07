"""
rs = []

for i in range(len(nums)):

    val=nums.pop(i)
    
    pr= 1
    for j in nums:
        pr *=j

    rs.append(pr)
    nums.insert(i, val)

print(rs)

"""

nums = [1,2,3,4]

rs = []

pre = 1   # prefixnusm * suffixsum 
suf= 1 

for i in range(len(nums)):
    fr = nums[0]

    if nums[i] == fr:
        pre = nums[i]
        rs.append(pre)
    else:
        pre *= nums[i-1]
        rs.append(pre)

    
for j in range(len(nums)-1,-1,-1):
    rs[j] = rs[j]* suf
    suf = suf *nums[j]

print(rs)

