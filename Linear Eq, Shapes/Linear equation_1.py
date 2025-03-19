numb_1=input("Enter a equation eg. 5 x - 2=18:")

array_a = numb_1.split("=")
lhs=array_a [0]
rhs=array_a [1]

array_b= lhs.split(" ")
num=array_b [0]
var=array_b [1]
sign=array_b[2]
inte=array_b[3]
if sign=='-':
     result= (int(rhs) + int(inte)) // int(num)
     print("The value is :x=",result)
elif sign=='+':
     result= (int(rhs) - int(inte)) // int(num)
     print("The value is :x=",result)
