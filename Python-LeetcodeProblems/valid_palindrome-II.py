s =list( "aba       ")

rev = s[::-1]

if rev == s:
    print("True")

elif rev != s:
    l =0
    r = len(s)-1

    for i in range(len(s)):
        if s[l]==s[r]:
            l+=1
            r-=1
        else:

            s.pop(r)
            break


    if s == s[::-1]:
        print(True)

    else:
        print(False)

