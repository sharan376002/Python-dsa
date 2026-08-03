nums = [3,1,2,4]

ev =[]
od =[]

for i in nums:
    if i%2==0:
        ev.append(i)
    else:
        od.append(i)


par = ev + od
print(par)