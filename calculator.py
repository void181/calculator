from replit import clear
from art import logo
def add(n1, n2):
    return n1 + n2

def  sub(n1, n2):
      return n1 - n2

def mul(n1, n2):
      return n1 * n2

def div(n1, n2):
      return n1 / n2
 
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
              }

    
def cal():
  
  print(logo)  
  num1 = int(input("What's the first number?: "))
  
  for symbol in operations:
      print(symbol)
  
  operation_symbol = input("Pick an operation from the line above: ")
 
  calculation_function = operations[operation_symbol]
  num2 = int(input("What's the second number?: "))

  answer = calculation_function(num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  ask = input("Do you want to continue? Type 'y' or 'n'")
  
  
  while ask == "y":
      num3 = int(input("What's the next number?: "))
      operation_symbol = input("Pick an operation from the line")
      calculation_function= operations[operation_symbol]
      print(f"{answer} {operation_symbol} {num3} ")
      answer = calculation_function(answer, num3)
      print(f"= {answer}")
      ask = input("Do you want to continue? Type 'y' or 'n'")
      # if ask == "n":
  
  
      #   print("Thank you for using the calculator")
        

  while ask=="n":

      user= input("Do you want to start  the new calculator? Type 'y' or 'n'")
      if user == "y":
            clear()
            cal()
                
      else:
            print("Thank you for using the calculator")
            return()

cal()
