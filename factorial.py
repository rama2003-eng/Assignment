def factorial(n):
    fact=1
    for i in range(1, n+1):
        fact=fact*i
    return fact 

number=int(input("Please enter any number to find factorial: "))

res=factorial(number)

print("The factorial of %d = %d"%(number,res))
