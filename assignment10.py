#bubble sort
numofstud=int(input("Enter the number of students "))
perc=[]
for i in range(0,numofstud):
  perc.append(int(input("Enter the percentages of students ")))
print(perc)

#sort
for i in range(0,numofstud-1):
  for j in range(0,numofstud-1):
    if perc[j]>perc[j+1]:
      perc[j+1],perc[j]=perc[j],perc[j+1]
    else:
      continue
print(perc)
for i in range(numofstud-1,numofstud-6,-1):
  print(perc[i])

  
  
  numofstud=int(input("Enter the number of students "))
perc=[]
for i in range(0,numofstud):
  perc.append(int(input("Enter the percentages of students ")))
print(perc)
#bubble sort using while
i=0
j=1
temp=0
while i<=(2*numofstud-1):
  if j==numofstud or i==numofstud:
    if i==numofstud:
      i=0
    elif j==numofstud:
      j=0
    temp=temp+1
    if temp==5:
      break
  if perc[i]>perc[j]:
    perc[i],perc[j]=perc[j],perc[i]
    i=i+1
    j=j+1
    print(perc)
    continue
  else:
    i=i+1
    j=j+1
    print(perc)
