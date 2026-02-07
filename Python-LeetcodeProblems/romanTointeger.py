d= {
 'M': 1000,
 'CM': 900,
 'D': 500,
 'CD': 400,
 'C': 100,
 'XC': 90,
 'L': 50,
 'XL': 40,
 'X': 10,
 'IX': 9,
 'V': 5,
 'IV': 4,
 'I': 1
}

s = "MCMXCIV"
rs =0
l=0

while l<len(s):
    if s[l:l+2] in d:
        rs+= d[s[l:l+2]]
        l+=2
    else:
        rs+=d[s[l]]
        l+=1
    
    
print(rs)
