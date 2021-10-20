def func(a,l):
  for i in range(l):
      num=int(input("Enter number of players "))
      a.append(num)
  return a

def display(q,l):
  for i in range(len(q)):
    print(q[i])
  
l=int(input("Enter the number of cricket players "))
k=int(input("Enter the number of badminton players "))
p=int(input("Enter the number of football players "))

crick=[]
badm=[]
foot=[]
q=func(crick,l)
w=func(badm,k)
e=func(foot,p)
print(q)
print(w)
print(e)

#union-play either cricket or badminton
union=q
for i in q:
  if i not in union:
    union.append(i)
print(union)

#intersection-play both cricket and badminton
intersection=[]
for i in range(0,l):
  count=0
  for j in range(0,k):
    if (q[i]==w[j]):
      count=+1
      if count>0:
        intersection.append(w[j])
print(intersection)

#difference-play cricket but not badminton
diff=[]
for i in q:
  if i not in w:
    diff.append(i)
print(diff)
