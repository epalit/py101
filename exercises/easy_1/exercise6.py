end_int = int(input("Please enter an integer greater than 0: "))
operation = input('Enter "s" to compute the sum, or "p" to compute the product. ')

if operation == 's':
    result = sum(range(1, end_int+1))
    print(f"The sum of the integers between 1 and {end_int} is {result}.")
else:
    result = 1
    for num in range(1,end_int+1):
        result *= num
    print(f"The product of the integers between 1 and {end_int} is {result}.")
