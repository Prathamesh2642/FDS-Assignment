#sentinel search
b=[]
noofstud=int(input("Enter the number of students "))
for i in range(0,noofstud):
  b.append(int(input("Enter the roll numbers ")))
print(b)
ssearch=int(input("Enter the roll number to be searched "))
if (ssearch==b[noofstud-1]):
  print(f"found at position {noofstud-1}")
else:
  b[noofstud-1]=ssearch
  print(b)
  for i in range(0,len(b)-2):
    if(i==b[noofstud-1]):
      print(f"Found at position {i}")
