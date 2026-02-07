p = [3,3,4,5] # 3,3,4,5
li=5

p.sort()

boats = 0

l=0
r = len(p)-1

while l<=r:
    sums = p[l]+ p[r]
    if l<r and  sums>li:
        boats+=1
        r-=1
    elif l<r and sums <=li:
        boats +=1
        l+=1
        r -=1
    else:
        boats+=1
        break
        

print(boats)

    


