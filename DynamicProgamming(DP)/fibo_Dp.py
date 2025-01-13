# find the 9th position of fibonacci



# bottom-up approach
def fibo(position):
    dp = [0]*position
    dp[0] = 1
    dp[1]=1
    for i in range(2,position):
        dp[i] = dp[i-1]+dp[i-2]

    print(f"fibo{position} is {dp[-1]}")    

    