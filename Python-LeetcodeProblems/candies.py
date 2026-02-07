candies = [2,3,5,1,3]
extra = 3


result = []
maxe =  max(candies)


for i in range(len(candies)):
     sum = candies[i] + extra
     if sum < maxe:
          result.append( False)
     else:
          result.append(True)


print(result)