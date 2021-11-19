#merge sort

def merge(arr):
  if len(arr)>1:
    mid=(len(arr))//2
    lower=arr[:mid]
    upper=arr[mid:]
    print(lower)
    print(upper)
    merge(lower)
    merge(upper)

    i,j,k=0,0,0
    while i<len(lower) and j<len(upper):
      print(lower)
      if lower[i]<upper[j]:
        arr[k]=lower[i]
        i=i+1
      else:
        arr[k]=upper[j]
        j=j+1
      k=k+1
      
    while j<len(upper):
      arr[k]=upper[j]
      j=j+1
      k=k+1
      print(arr)
      
    while i<len(lower):
      arr[k]=lower[i]
      i=i+1
      k=k+1
      print(arr)

    return arr
num=int(input("Enter the number of entries "))
arr=[]
for i in range(num):
  a=int(input("Enter the numbers "))
  arr.append(a)
newlist=merge(arr)
print(newlist)
