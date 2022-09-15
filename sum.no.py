a=int(input('enter a no:--'))
i=1
while i<=3:
    if a%4==0:
        print(a,end=" ")
        a=a-4
    else:
        print(a,end=" ")
        a=a+4
    i=i+1
    print()