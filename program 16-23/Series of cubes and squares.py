num_1 = int(input("Enter the starting number(square): "))
num_2= int(input("Enter the last number(square): "))
num_3 = int(input("Enter the starting number(cube): "))
num_4= int(input("Enter the last number(cube): "))

print("The squares are:")
for i in range(num_1, num_2+1):
    print(i*i)

print("The cubes are:")
for i in range(num_3, num_4+1):
    print(i*i*i)
