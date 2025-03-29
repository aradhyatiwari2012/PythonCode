num_1 = input("Enter the length, breadth and height of cuboid separated by commas: ")
array_a = num_1.split(",")
l = int(array_a[0])
b = int(array_a[1])
h = int(array_a[2])

LSA = 2 *(l + b)*h
TSA = 2 *(l * b + b * h + l * h)
VOL = l * b * h


print("The lateral surface area is:", LSA, "square units")
print("The total surface area is:", TSA, "square units")
print("The volume is:", VOL, "cubic units")
