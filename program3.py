print("Marksheet")
a=int(input("Enter your java marks: "))
b=int(input("Enter your j2ee marks: "))
c=int(input("Enter your python marks: "))
d=int(input("Enter your php marks: "))
e=int(input("Enter your cybers marks: "))
total=(a+b+c+d+e)
print("Your Total marks: ",total)
avg=(total/500)*100
print("Your Avg %: ",avg)
if(avg>=90 and avg<100):
    print("Your Grade is A")
elif(avg>=80 and avg<90):
    print("Your Grade is B")
elif(avg>=70 and avg<80):
    print("Your Grade is C")
elif(avg>=60 and avg<70):
    print("Your Grade is D")
elif(avg>=40 and avg<60):
    print("Your Grade is E")
else:
    print("you Fail")
