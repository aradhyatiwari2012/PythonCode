num_1 = input("Enter the radius and height of the cylinder: ")
array_a = num_1.split(",")
r = int(array_a[0])
h = int(array_a[1])

LSA = 2 * 3.14 * r * h
TSA = 2 * 3.14 * r * (h + r)
VOL = 3.14 * r**2 * h


print("The lateral surface area is:", LSA, "square units")
print("The total surface area is:", TSA, "square units")
print("The volume is:", VOL, "cubic units")
