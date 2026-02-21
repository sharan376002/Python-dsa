def checkInclusion(s1: str, s2: str) -> bool:

        n1= len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        cnt1 = [0]*26
        cnt2 = [0]*26

        for i in range(n1):
            cnt1[ord(s1[i]) - ord('a')] +=1
            cnt2[ord(s2[i]) - 97] +=1
        

        if cnt1 == cnt2:
            return True

        for i in range(n1,n2):
            cnt2[ord(s2[i]) - 97] += 1
            cnt2[ord(s2[i-n1]) - 97] -=1

            if cnt1 ==cnt2:
                return True
        
        return False
        

s1 = "ab", s2 = "eidbaooo"
checkInclusion(s1,s2)