#String with most number of letters
a=input("Enter the string ")
c=[]
c=a.split()
temp=0
for i in range(len(c)):
  if temp<len(c[i]):
      temp=len(c[i])
      word=c[i]
print(f"{temp} for {word}")

#Count apperance of a character
b=input("Enter the character  ")
count=0
for i in a:
  if i==b:
    count=count+1
print(count)

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
