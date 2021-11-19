numofstud1=int(input("Enter the number of students "))
perce=[]
for i in range(0,numofstud1):
  perce.append(int(input("Enter the percentages of students ")))
print(perce)
#selection sort
for i in range(numofstud1-1):
  min=perce[i]
  for j in range(i+1,numofstud1):
    if perce[j]<min:
      min=perce[j]
      perce[i],perce[j]=perce[j],perce[i]

print(perce)
