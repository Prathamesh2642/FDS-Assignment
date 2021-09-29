#Practical 4
bal=0
n=100
for i in range(n):
  a=input("Enter operation and value ")
  b=[]
  b=a.split()
  operation=b[0]
  temp=b[1]
  value=int(temp)
  if (operation=='D'):
    bal=bal+value
  elif (operation=='W'):
    if(bal>value):
      bal=bal-value
  else:
    print("Insufficient balance")
  c=input("Do you want to continue with next transaction ")
  if (c=='yes' or c== 'y'):
    pass
  elif(c=='no' or c=='n'):
    break
print(f"Balance is {bal}")
