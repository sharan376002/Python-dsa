word1 = "abcd"
word2 = "pq"

final = []

l=0
r=0

while l<len(word1)  and r<len(word2):

    final.append(word1[l])
    final.append(word2[r])
    l+=1
    r+=1

final.extend(word1[l:])
final.extend(word2[r:])


s = "".join(final)
print(str(s))
