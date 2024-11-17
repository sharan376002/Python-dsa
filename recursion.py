#  the functionthat calls itesel is called recursion

# finding the factorial using a recursion   LOGIC  :  n*(N-1)!


n= 10
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(n))