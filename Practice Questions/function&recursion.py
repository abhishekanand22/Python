
# questions on Functions


def calc_avrage(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)


def calc_factorial(n):
    fact=1
    for i in range (1,n+1):
        fact*=i
    print(fact)


def usd_to_inr(n):
    usd= n*83
    print(usd)


def odd_even(n):
    if n%2==0:
        print("Even")
    else:
        print("odd")


def palindrone(n):
    num=str(n)
    if str(n) == num[::-1]:
        print("Palindrone")
    else:
        print("Not a Palindrone")

palindrone(12)        
odd_even(23)
usd_to_inr(100)
calc_factorial(5)
calc_avrage(1,2,3)


print("--------------------")

# Recursion Questions 


def show(n):
    if n==-1:
        return
    print(n)
    show(n-1)



def factorial(n):
    if n == 0 or n == 1:
        return 1

    return factorial(n - 1) * n


def calc_sum(n):
    if n==0:
        return 0
    print(n)
    return calc_sum(n-1)+n


def print_list(lst, idx=0):
    if idx == len(lst):
        return
    print(lst[idx])
    print_list(lst, idx + 1)
fruits = ["mango", "litchi", "apple", "banana"]



print_list(fruits)
show(6)
print(factorial(5))
sum=calc_sum(10)
print(sum)
