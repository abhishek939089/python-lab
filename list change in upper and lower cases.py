n=int(input("Enter no. of elements:"))
a=list(map(str,input("Enter elemenst:").strip().split()))
print("list is==>",a)
yup=list(map(lambda a:str.upper(a),a))
print(yup)