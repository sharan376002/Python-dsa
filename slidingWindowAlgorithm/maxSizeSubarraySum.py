# it is a leetcode problem 209


target = 7
nums = [2,3,1,2,4,3]

left = 0
right = 0

mini = []
subsum = 0
while right<len(nums):
    subsum +=nums(right)

    while subsum >= target:
        mini.append(right-left+1)
        subsum -= nums(left)
        left +=1
    right +=1
    
0 if len(mini)==0 else min(mini)