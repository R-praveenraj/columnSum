# #You are given a 2D integer matrix A, return a 1D integer array containing column-wise sums of original matrix.
# Input
# [ [1,2,3,4]
#   [5,6,7,8]
#   [9,2,3,4] ]

# Output
# [15, 10, 13, 16]
def columnSum(array,row,column):
    sum=[]
    for i in range(column):
        total=0
        for j in range(row):
            total+=array[j][i]
        sum.append(total)
    return sum


array=[]
row=int(input())
column=int(input())
for i in range(row):
    array.append(list(map(int,input().split())))
print(columnSum(array,row,column))