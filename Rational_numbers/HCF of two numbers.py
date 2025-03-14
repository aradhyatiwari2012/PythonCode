def hcf(a,b):
    for i in range(max(a, b), 1 + (a * b)):
         if i % a == i % b == 0:
             return i
             

n1 = int(input("Enter 1st no."))
n2 = int(input("Enter 2nd no."))
a=n1
b=n2
c=hcf(a,b)
hcf12=(a*b)//c
print("HCF of", a, "and", b, "is", hcf12)

       

