def iseven(n):
    if n % 2 == 0:
        return True
    else:
        return False

def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print()
print("Tyepe (iseven) To check your number is even or odd.")
print("Type (factorial) To calculate the factorial of your number. \n")
print("Type (isprime) To check your number is prime or not. ")
print("Type (exit) To exit the program. \n")







while True:
    op = input("Please select the operation: ")

    if op == "iseven":
        n = int(input("Enter a number: "))
        if iseven(n):
          print(f"{n} is even.")

        else:
          print(f"{n} is odd.")


    elif op == "factorial":
        n = int(input("Enter a number: "))
        print(f"{n} factorial of {factorial(n)}")


    elif op == "isprime":
        n = int(input("Enter a number: "))

        if isprime(n):
            print(f"{n} is prime.")

        else:
            print(f"{n} is not prime.")


    elif op == "exit":
        print("Good Bye!")
        break

    else:
        print("Invalid operation.")
