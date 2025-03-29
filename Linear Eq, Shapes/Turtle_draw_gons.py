import turtle  

def ext_ang(n):
    var_1 = 360//n
    return var_1

def draw_gon(sides, units, angles):
    t = turtle.Turtle()
    t.speed(3)

    for _ in range(sides):  
        t.forward(units)
        t.right(angles)

    turtle.done()

side = int(input("Enter the number of sides: "))  
ang = ext_ang(side)
units = int(input("Enter the number of units by which you want to draw the line: "))

draw_gon(side, units, ang)
