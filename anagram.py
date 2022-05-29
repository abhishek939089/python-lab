n=list(input("Enter string "))
m=list(input("Enter 2nd string "))
n.sort()
m.sort()
if (n==m):
    print("Anagram")
else:
    print("Not Anagram")