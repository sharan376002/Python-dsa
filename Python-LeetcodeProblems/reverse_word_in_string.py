s = "the sky is blue"


l=0
r=1

# while r<len(s):

#     if s[r]==" ":
#         s[l:r]


w=  s.split()
rs = " ".join(w[1:] + w[:1])
print(rs)


# for i in range(len(w)):
#     print(w[i])