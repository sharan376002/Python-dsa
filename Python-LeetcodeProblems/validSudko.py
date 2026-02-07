board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


import collections

r = collections.defaultdict(set)
c = collections.defaultdict(set)
s = collections.defaultdict(set)


for row in range(9):
    for col in range(9):

        if board[row][col] == ".":
            continue

        val = board[row][col]

        if val in r[row] or val in c[col] or val in s[row//3,col//3]:
            print("false  it is not valid ")

        r[row].add(val)
        c[col].add(val)
        s[row//3,col//3].add(val)

print("it is valid ")

