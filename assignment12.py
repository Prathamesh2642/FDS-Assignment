def Insertionsort(perce):
    for i in range(1, len(perce)):
        temp = perce[i]
        j = i - 1
        while j > 0 and temp < perce[j]:
            perce[j + 1] = perce[j]
            j = j - 1
        perce[j + 1] = temp

numofstud1=int(input("Enter the number of students "))
perce=[]
for i in range(0,numofstud1):
  perce.append(int(input("Enter the percentages of students ")))
print(perce)
Insertionsort(perce)
print(perce)
