def fraction(variable1):
    fraction=variable1.split("/")
    return(fraction)

numb_1=input("Write the fraction:")

num_a=fraction(numb_1)[0]
den_b=fraction(numb_1)[1]

num_1=int(num_a)*-1

print("The additive inverse is:",num_1,"/",den_b)

