a=input("Enter the string ")
c=[]
c=a.split()
temp=0
for i in range(len(c)):
  if temp<len(c[i]):
      temp=len(c[i])
      word=c[i]
print(f"{temp} for {word}")

b=input("Enter the character  ")
count=0
for i in a:
  if i==b:
    count=count+1

print(count)

#Enter substring
c=input("Enter the substring ")
e=0
for i in range(len(a)-1):
  if (a[i]==c[e]):
    e=e+1
    if(e==len(c)):
      break
  if len(c)==0:
    break

if(e<len(c)):
  print("not present")
else:
  k=i-e+1
  print(f"{c} is present at position {k}") 

#To check string is palindrom or not
a=input("Enter the string ")
b=input("Enter another string ")
c=''
for i in range(len(b)-1,-1,-1):
  c=c+b[i]
if(a==b):
  print("Palindrome")
else:
  print("Not a palindrome")
