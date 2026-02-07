nums = [1,7,3]

mid  = len(nums)
print(mid)


left  =   sum(nums[:mid])
right  =  sum(nums[mid+1:])


if left == right:
    print(mid)




print(left , right )

