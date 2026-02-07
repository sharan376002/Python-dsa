strs = ["eat","tea","tan","ate","nat","bat"]

dic = {}


for i in range(len(strs)):

    so = "".join(sorted(strs[i]))
    
    if so not in dic:
        dic[so] = [strs[i]]
    
    else:
        dic[so].append(strs[i])


v = list(dic.values())
print(v)


print(dic)



