# some practice questions on loops 


# print reverse counting 
def reverseCounting(n):
    i = n
    while i >= 1:
        print(i)
        i -= 1


# print multiplication table of n
def multiplicationTable(n):
    i=1
    x=10
    while i<=x:
        print(n ,"*", i, "=", i*n)
        i+=1

if __name__ == "__main__":
    n = int(input("Enter n: "))
    reverseCounting(n)
    multiplicationTable(n)


# search in tuple
t = (2, 3, 4, 5, 6, 7, 8, 9)
i = 0
while i < len(t):
    if t[i] == 2:
        print("Found at", i)
    else:
        pass
    i += 1

