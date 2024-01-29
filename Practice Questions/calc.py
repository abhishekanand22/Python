# Basic Calculator 

def calculator(a,b,opr):
    if opr == "+":
        print("Sum = ",a+b)
    elif opr == "-":
        print("Subtraction = ",a-b)
    elif opr == "*":
        print("Multiplication = ",a*b)
    elif opr == "/":
        print("Division = ",a/b)
    elif opr == "%":
        print("Percentage = ",(a/100)*b,"%")
    else :
        print("Invalid Operation")


if __name__ == "__main__":
    a=int(input("First Number : "))
    b=int(input("Second Number : "))

    opr=input("Choose Operation (+ , - , * , / , % ) : ")

    if opr == "%":
        print("In Percentage 'a' should be percent & 'b' should be total ")
    else:
        pass

calculator(a,b,opr)

