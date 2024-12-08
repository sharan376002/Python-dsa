from collections import deque

stack = [1,2,3,4,5,6,7]

print(stack[-1])  # accesing

stack.append(8)

print(stack[-1])  # push

stack.pop()

print(stack[-1])  # delete

x=7
if x==7 in stack:  # searching
    print(True)

# stack by module
stack_mod = deque([1,2,3,4,5,6,7])
print(stack_mod)


