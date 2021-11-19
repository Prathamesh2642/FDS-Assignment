#Binary search
def Binarysearch(c,bsearch):
  first=0
  last=noofstud-1
  mid=0
  while first<=last:
    middle=((first+(last))//2)
    if bsearch not in c:
      return -1
    elif(c[middle]==bsearch):
      return middle
    elif(c[middle]<bsearch):
      first=middle
    elif(c[middle]>bsearch):
      last=middle
    if bsearch not in c:
      return -1
c=[]
noofstud=int(input("Enter the number of students "))
for i in range(0,noofstud):
  c.append(int(input("Enter the roll numbers in sorted order ")))
print(c)
bsearch=int(input("Enter the roll number to be searched "))



a=Binarysearch(c,bsearch)
if a==-1:
  print("Not found")
else:
  print(f"{bsearch} is present at {a}")
  
  
  
  
