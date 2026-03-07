

# give a transpose -> then horizontal reflection of it then it rotated as image 


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

n = len(matrix)
# transpose 


for i in range(n):
    for j in range(i+1 ,n):

        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]


# horizontal reflection 


for i in range(n):
    for j in range(n//2):
        matrix[i][j],matrix[i][n-j-1] = matrix[i][n-j-1],matrix[i][j]



print(matrix)