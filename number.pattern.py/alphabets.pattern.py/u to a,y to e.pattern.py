# n=int(input("enter a no:--"))
# v=ord("U")
# i=0
# while i<n:
#     j=0
#     while j<n:
#         print(chr(v),end=" ")
#         v=v+1
#         j=j+1
#     i=i+1
#     v=v-10
#     print()

n=5
v=ord("u")
for i in range(n):
    for j in range(n):
        print(chr(v),end=" ")
        v=v+1
    v=v-10
    print()