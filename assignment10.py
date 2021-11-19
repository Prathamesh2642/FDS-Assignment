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
