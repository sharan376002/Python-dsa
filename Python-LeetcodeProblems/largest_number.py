nums = [3,30,34,5,9]


nums = list(map(str,nums))

rs = []

nums.sort(key=lambda x: x*10,reverse=True)


for i in range(len(nums)):
    sus = rs.append(nums[i])


s="".join(rs)
print(s)