# Nested if
age=int(input("Enter your Age : "))
eatPizza=input("Are you PiZzA,Type 'Yes' or 'No' : ")
exercise=input("If u workout daily, Type 'Yes' or 'No' : ")
if(age<30):
        if eatPizza=="Yes"or eatPizza =="yes" or eatPizza == "YES" :
            print("Unfit")
        else:
            print("Fit")
else:
        if exercise=="Yes" or exercise=="YES" or exercise=="yes":
            print("fit")
        else:
            print("Unfit")
#Ternary operator
print( "child" if (age<18) else "Adult")
#Wrie above program in simple statement using ternary operator
