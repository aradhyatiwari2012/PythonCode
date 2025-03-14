def fraction(variable1):
    fraction=variable1.split("/")
    return(fraction)

def lcm(a,b):
    for i in range(max(a, b), 1 + (a * b)):
         if i % a == i % b == 0:
             return i
numb_1=input("Write the 1st fraction:")
numb_2=input("Write the 2nd fraction:")
find_ra=input("Write the no. of rational numbers you need to find:")

num_1=int(fraction(numb_1)[0])
num_2=int(fraction(numb_2)[0])

den_1=int(fraction(numb_1)[1])
den_2=int(fraction(numb_2)[1])
ra_1=int(find_ra) + 1

lcm_num=int(lcm(den_1,den_2))

den_a=int(lcm_num)/int(den_1)
den_b=int(lcm_num)/int(den_2)

num_a=int(num_1)*int(den_a)
num_b=int(num_2)*int(den_b)

num1= int(num_a)* int(ra_1)
num2= int(num_b)* int(ra_1)
den= int(lcm_num)* int(ra_1)

print("The numbers in between are:")
for i in range(num1,num2-1):
    print(i,"/",den)
