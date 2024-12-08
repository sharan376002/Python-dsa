#  the functionthat calls itesel is called recursion

# finding the factorial using a recursion   LOGIC  :  n*(N-1)!

"""
the breakdown of the recursion  , 5*4! => 4*3!=>, 3*2! => 2*1!  here how the code works , it breakdown th problem
"""
n= 5
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)  # the values stores in the stack

print(fact(n))



# recursion is the impotartant topic please solve problems on it...