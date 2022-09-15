n=int(input("enter a no"))
row=0
while row<n:
    star=row+1
    while star>0:
        print("*",end=" ")
        star=star-1
    row=row+1
    print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("\n")