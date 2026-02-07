haystack = "sadbutsad"
needle = "sade"

l = 0

r = 0

rs = []

for l in range(len(haystack)):

    r = 0
    rs = []  # --->> reseting it 

    while l+r <len(haystack)  and r<len(needle) and haystack[l+r] == needle[r]:

        rs.append(haystack[l+r])
        r+=1


    rs = "".join(rs)


    if rs == needle:
        print(l)
        break

else:
    print(-1)

