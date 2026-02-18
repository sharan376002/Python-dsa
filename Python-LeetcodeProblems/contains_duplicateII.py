nums = [1,2,3,1]
k = 3

l=0
r=0

dup = set()

while r<len(nums):

    if nums[r] in dup:
        print(True)

    dup.add(nums[r])

    if (r-l)>=k:
        dup.remove(nums[l])
        l+=1

    r+=1

print(False)