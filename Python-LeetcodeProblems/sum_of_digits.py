# Sun of the digits
num = int(input("Enter the number to sum the digits :")) # 1234

x = num//1000 # it gives 1
x1 = (num-x*1000)//100  # 2
x2 = (num-x*1000-x1*100)//10#3
x3 = (num-x*1000-x1*100 - x2*10) #4

print(x+x1+x1+x3)

