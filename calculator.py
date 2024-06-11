num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation +, -, *, /, //, %, &, or : ")


def calculator(num1, num2, operation):
    if operation == "+":
      return num1 + num2
    elif operation == "-":
       return num1 - num2
    elif operation == "*":
       return num1 * num2
    elif operation == "/":
       if num2 == 0:
        return "invalid input"
       else:
        return(num1 / num2) 
    elif operation == "//":
      if num2!=0:
        return(num1 // num2)
      else:
        return("invalid input")
    elif operation == "%":
      if num2!=0:
        return(num1 % num2)
      else:
        return("invalid input")
    elif operation == "&":
      return (num1 & num2)
    elif operation == "or":
      return (num1 or num2)
    else:
      return "invalid operation"
    
result = calculator(num1, num2, operation)
print(result, "is the result")
    
     
     
 