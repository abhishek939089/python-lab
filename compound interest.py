P=float(input("Enter the Principle amount to be compounded annually\n"))
R=float(input("Enter the rate of interest\n"))
T=float(input("Enter the time period\n"))
Q=(1+0.01*R)**T
ci=P*Q - P
A=P*Q
print("The compound interest is ",ci)
print("The amount is ",A)