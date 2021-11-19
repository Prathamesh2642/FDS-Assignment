#linear search
a=[]
noofstud=int(input("Enter the number of students "))
for i in range(0,noofstud):
  a.append(int(input("Enter the roll numbers ")))
print(a)
lsearch=int(input("Enter the roll number to be searched "))
count=0
for i in range(noofstud):
  if(a[i]==lsearch):
    count=1
    break
  else:
    count=0
if(count==1):
  print(f"Roll number found at position {i}")
else:
  print("Not found")
