n=int(input("enter a no:---"))
for i in range(n):
    for j in range(i+1):
        print(i+1,end=' ')
    for j in range(n):
        print("*",end=" ")
    print()