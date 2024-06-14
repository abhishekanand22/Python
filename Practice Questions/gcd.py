
#using math builtin function 
import math
def g_c_d(a,b):
    return math.gcd(a,b)

a=12
b=37
print("GCD = ",g_c_d(a,b))


# using euclidien division

print("using euclidien division")

def gcd_euclidean(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = 48
num2 = 18
print(f"The GCD of {num1} and {num2} is {gcd_euclidean(num1, num2)}")



# using recurrsion

print("Using Recurrsion")
def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

num1 = 48
num2 = 18
print(f"The GCD of {num1} and {num2} is {gcd_recursive(num1, num2)}")

