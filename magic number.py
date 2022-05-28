x=int(input("Enter the number:"))
i=1
sum1=0
sum2=0
while(i<=10):
    if (i%2==0):
        sum1=sum1+x%10
        x=x//10
    else:
        sum2=sum2+x%10
        x=x//10
    i=i+1
if(sum1==sum2):
    print("Magic number:")
else:
    print("Not magic number:")