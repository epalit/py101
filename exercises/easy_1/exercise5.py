bill_amount = float(input("What is the bill? "))
tip_percentage = float(input("What is the tip percentage? "))

tip = bill_amount * (tip_percentage / 100)

total = bill_amount + tip

print(f"The tip is ${tip}")
print(f"The total is ${total}")
