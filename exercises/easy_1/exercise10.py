def multisum(max_num):
    total = 0
    for num in range(1, max_num + 1):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    
    return total

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)