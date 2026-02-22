s = "AABABBA"
k = 1

longest = 0

l=0

cnt  = [0]*26

for r in range(len(s)):

    cnt[ord(s[r]) - 65] +=1

    while (r-l+1) - max(cnt) > k:
        cnt[ord(s[l]) - 65] -=1
        l+=1

    longest = max(longest,r-l+1)

print(longest)
