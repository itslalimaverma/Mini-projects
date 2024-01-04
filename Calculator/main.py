from replit import clear
from art import logo
print(logo)

def add(n1, n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

newdic={}
newdic["+"]=add
newdic["-"]=subtract
newdic["*"]=multiply
newdic["/"]=divide

def calculator():
  num1=int(input("Enter first number: "))
  for i in newdic:
    print(i)
  work_finished=True
  
  while work_finished:
    operation_sym=input("Choose an operation: ")
    num2=int(input("Enter next number: "))
    calculation_fucntion=newdic[operation_sym]
    first_ans=calculation_fucntion(num1,num2)
    print(f"{num1} {operation_sym} {num2} = {first_ans}")
  
    print("Type 'y' to continue calculating, 'n' to start a new calculation.")
    user_input=input("")
  
    
    if user_input=="y":
      num1=first_ans
    else:
      work_finished=False
      clear()
      calculator()

calculator()


# --------------------------------
# if operation_sym=="+":
#   print(f"{num1} + {num2} = {add(num1,num2)}")
# elif operation_sym=="-":
#   print(f"{num1} - {num2} = {subtract(num1,num2)}")
# elif operation_sym=="*":
#   print(f"{num1} * {num2} = {multiply(num1,num2)}")
# elif operation_sym=="/":
#   print(f"{num1} / {num2} = {divide(num1,num2)}")
# else:
#   print("Invalid Operation")


# or

# calculation_fucntion=newdic[operation_sym]
# first_ans=calculation_fucntion(num1,num2)

# print(f"{num1} {operation_sym} {num2} = {first_ans}")




  