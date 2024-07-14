print("Calculater")
print("1 = add")
print("2 = sub")
print("3 = mul")
print("4 = div")
choice=(input("choice your number 1/2/3/4: "))
a=float(input("Enter your first number: "))
b=float(input("Enter your second number: "))
def calc(choice):
    if(choice=='1'):
        print(a+b)
    elif(choice=='2'):
        print(a-b)
    elif(choice=='3'):
        print(a*b)
    elif(choice=='4'):
        print(a/b)
    else:
        print("choice only 1 to 4")
calc(choice)
