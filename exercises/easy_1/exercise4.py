length = float(input("Enter room length in m:\n"))
width = float(input("Enter room width in m:\n"))

area = length * width
area_feet = area * 10.7639

print(f"The area of the room is {area:.2f} square meters "
      f"({area_feet:.2f} square feet).")