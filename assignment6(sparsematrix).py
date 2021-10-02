#Sparse Matrix
import array as arr
for h in range(0,1):
  row=int(input("enter no of rows "))
  col=int(input("enter no of cols "))
if (row==col):
  pass
else:
  print("enter a square matrix")


def creatematrix():
  for i in range(row):
    a=arr.array('i',[])
    a=[]
    for j in range(col):
      a.append(int(input()))
    matrix.append(a)
  
  return (matrix)
matrix=[]
matrix=creatematrix()

for i in range(row):
  print(matrix[i])

print("Row \t column \t value ")
for i in range(row):
  for j in range(col):
    if matrix[i][j]==0:
      continue
    else:
      print(i,"\t\t",j,"\t\t",matrix[i][j])
