a={}
m,n=input("Enter rows and columns of matrix").split(',')
m=int(m)
n=int(n)

for i in range(m):
    for j in range(n):
        a[(i,j)]=int(input(f'Enter {i}X{j}'))
print(a)