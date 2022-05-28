first = int(input("Enter first alement:"))
operator = input("Enter operator (+,-,*,/) :")
second = int(input("Enter second number:"))
if (operator == "+"):
   print(first + second)
elif (operator == "-"):
    print(first - second)
elif (operator == "*"):
    print(first * second)
elif (operator == "/"):
    print(first / second)
elif(operator == "%"):
    print(first % second)
else:
    print("invalid operation try again....")