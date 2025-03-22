def int_ang(n):
    var_1=(n-2)*180// n

    return var_1

num=int(input("Enter the no. of sides:"))
result=int_ang(num)
print("The interior angle of",num,"sided polygon is:",result)
