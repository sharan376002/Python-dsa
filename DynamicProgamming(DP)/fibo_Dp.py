# find the 9th position of fibonacci



# bottom-up approach
def fibo(position):
    dp = [0]*position
    dp[0] = 1
    dp[1]=1
    for i in range(2,position):
        dp[i] = dp[i-1]+dp[i-2]

    print(f"fibo{position} is {dp[-1]}")    

#top down approach

def fibodw(position,memory={}):
    if position in  memory:
        return memory[position]
    if position<=2:
        return 1
    
    memory[position] = fibodw(position-1,memory) + fibodw(position-2,memory)

    return memory[position] 