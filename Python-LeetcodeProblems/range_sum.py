nums = [-2,0,3,-5,2,-1]
left = 0
right = 2
sums=0
nu = nums[left:right+1]
for i in range(len(nu)):
    sums += nu[i]

print(sums)