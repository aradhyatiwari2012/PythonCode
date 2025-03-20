numb_1=input("Input two fractions(for eg. 1/2,3/4):")
array_a = numb_1.split(",")
frac_1=array_a [0]
frac_2=array_a [1]

array_b= frac_1.split("/")
num_1=array_b [0]
den_1=array_b [1]

array_c= frac_2.split("/")
num_2=array_c [0]
den_2=array_c [1]

mul_1=int(num_1)*int(den_2)
mul_2=int(num_2)*int(den_1)

if mul_1==mul_2:
    print("The result is:",mul_1,"=",mul_2)

elif mul_1!=mul_2:
    print("The result is:",mul_1,"≠",mul_2)
