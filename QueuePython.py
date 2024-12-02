from queue import Queue


qu = []

#enqueue
qu.append(5)
qu.append(7)
qu.append(1)
qu.append(9)
qu.append(2)
print(qu)

#dequeue  
a = qu.pop(0)
b = qu.pop(0)
print(a,b)


# front
print(qu[0])

#is empty
print(len(qu)==0)
