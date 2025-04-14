def ascend(num):
    a = num.split(",")
    num1 = [int(x) for x in a]
    num1.sort()

    return num1

c = input("Enter the numbers: ")
d = ascend(c)
print(d)


