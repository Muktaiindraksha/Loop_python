n=int(input("enter the number:--"))
i=1
while i<=n: 
    j=n
    while j>i:
         print("",end=" ")
         j=j-1
    k=1
    while k<=j:
         print("*",end=" ")
         k+=1
    i+=1
    print()
o=1
while o<=5:
    l=1
    while l<=o:
        print(" ",end="")
        l=l+1
    m=4
    while m>=o:
        print("*",end=" ")
        m-=1
    o+=1
    print()