# string=input("enter a string:---")
# reversed_string=""
# for i in string:
#     reversed_string=i+reversed_string
# print("reversed_string",reversed_string)

a="she is good girl"
string=" "
i=len(a)-1
while i>=0:
    string=string+a[i]
    i=i-1
print(string)
