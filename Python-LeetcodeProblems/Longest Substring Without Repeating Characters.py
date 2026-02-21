s = "pwwkew"


se  = set()

l=0
r=0

length = 0

while r<len(s):
    if s[r] not in se:
        se.add(s[r])
        length = max(length, r-l+1)
        r+=1
    else:
        se.remove(s[l])
        l+=1


    

print(length)
    
print(se)