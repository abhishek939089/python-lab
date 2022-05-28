n=int(input("Enter the number:"))
sum =0
num=n
nu=0
c=0
while n!=0:
    n=n//10
    nu=nu+1
n=num
while n!=0:
    t=n%10
    s=t**nu
    n=n//10
    sum=sum+s
if (sum==num):
    print("Number is armstrong:")
else :
    print("Number is not armstrong:")