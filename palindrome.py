n=int(input("Enter the number:"))
rev=0
num =n
while n!=0:
    t=n%10
    rev=rev*10+t
    n=n//10
if (rev==num):
    print("palindrome number:")
else:
    print("Not palindrome:")