#PRACTICAL 1

l=[]
noofstudents=int(input("enter number of students: "))
for i in range(0,noofstudents):
  a=int(input(f"Enter marks of the student {i+1}"+': '))
  l.append(a)
print(l)
j=len(l)
def average():
  sum=0
  count=0
  for i in l:
    sum=sum+i
    count=count+1
  ave=sum/count
  print("Average score of the class is",ave)
 
def maximum():
  max=0
  for i in l:
    if (max<=i):
      max=i
  print("Maximum marks scored in the class is",max)

def minimum():
  min=l[0]
  for i in l:
    if(min>=i):
      min=i
  print("Lowest score in the class are",min)

def maxfreq():
  maxcount=0
  tem=0
  for i in range(0,len(l)):
    count=0
    for j in range(0,len(l)):
      if (l[i]==l[j]):
        count=count+1
    if (maxcount<=count):
       maxcount=count
       tem=l[j] 
  print(f"Maximum frequncy is of {tem} and it is {maxcount}")

average()
maximum()
minimum()
maxfreq()
