"""
'+'.
Record a new score that is the sum of the previous two scores.

'D'.
Record a new score that is the double of the previous score.

'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all t


"""

ops = ["5","2","C","D","+"]

sums=0

stack = []

for i in range(len(ops)):

    if ops[i] == "C":
        stack.pop()

    elif ops[i] == "D":
        stack.append(stack[-1]*2)

    elif ops[i] == "+":
        stack.append(stack[-1] + stack[-2])
    
    else:

        stack.append(int(ops[i]))

sums = sum(stack)
print(stack)
print(sums)