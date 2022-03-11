#pattern program in python...
no_rows = int(input("Enter the number of row :"))
for row in range (1, no_rows+1):
    for column in range (1, row+1):
        print("*", end=" ")
    print()