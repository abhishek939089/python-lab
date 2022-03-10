n=int(input("Enter the number : "))
n2=n**2
sum=0
a=0
while(n2!=0) :
    a=n2%10
    sum=sum+a
    n2 =n2 // 10

if (sum == n) :
    print("Yes my dear , it's a neon number ")
else :
    print("dear , it's not neon number try again.... ")