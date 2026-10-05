a=int(input("enter the number:"))
b=int(input("enter the number:"))
operator=input("enter operator:")
if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
elif operator=="/":
    print(a/b)
else:
    print("invalid operator")