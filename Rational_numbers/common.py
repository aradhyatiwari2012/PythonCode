def hcf(a,b):
    for i in range(max(a, b), 1 + (a * b)):
         if i % a == i % b == 0:
             return i
             


       

def lcm(a,b):
    for i in range(max(a, b), 1 + (a * b)):
         if i % a == i % b == 0:
             return i
             


       
def fraction(variable1):
    fraction=variable1.split("/")
    return(fraction)
