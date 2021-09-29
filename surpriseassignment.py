#Surprise Assignment
name=input("Enter your name: ")
print("Designation: \n 1.Manager \n 2.Team Leader \n 3.Team Member ")
desig=int(input("Enter designation "))
month=int(input("Enter the month number "))
if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or  month==12):
  days=int(input("Enter number of days you've worked "))
  if (days>31):
    print("Enter valid number of days")
  print("Have you worked overtime ")
  over=input()
  if(over=='yes'):
    overtimedays=int(input("Enter number of overtime days "))
    if((overtimedays+days>31)):
      print("Enter valid details")
  elif(over=='no'):
    pass
elif (month==4 or month ==6 or month==9 or month==11):
  days=int(input("Enter number of days you've worked "))
  if (days>30):
    print("Enter valid number of days")
  print("Have you worked overtime ")
  over=input()
  if(over=='yes'):
    overtimedays=int(input("Enter number of overtime days "))
    if((overtimedays+days)>30):
      print("Enter valid details")
elif (month==2):
  days=int(input("Enter number of days you've worked "))
  if(days>29):
    print("Enter valid number of days")
  print("Have you worked overtime ")
  over=input()
  if(over=='yes'):
    overtimedays=int(input("Enter number of overtime days "))
    if((overtimedays+days>29)):
      print("Enter valid details")

if (over=='yes'):
  if (desig==1):
    salary=(2000*days)+(1000*overtimedays)
  if (desig==2):
    salary=(1800*days)+(900*overtimedays)
  if (desig==3):
    salary=(1500*days)+(750*overtimedays)
elif(over=='no'):
  if (desig==1):
    salary=(2000*days)
  elif (desig==2):
    salary=(1800*days)
  elif (desig==3):
    salary=(1500*days)
print(salary)
