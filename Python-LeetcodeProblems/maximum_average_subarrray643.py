nums = [1,12,-5,-6,50,3]
k = 4

sums =0

avg =0

l=0

for r in range(len(nums)):
    sums  += nums[r]


    if r-l+1 >k:

        sums -= nums[l]
        l+=1

    if r-l+1 ==k:
        avg  = max(avg,sums/k)
        

print(avg)
        

