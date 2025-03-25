import turtle  

def int_ang(n):
    var_1 = (n - 2) * 180 // n
    return var_1

def draw_gon(sides, units, angles):
    t = turtle.Turtle()
    t.speed(3)

    for _ in range(sides):   # Use 'sides' here, not 'side'
        t.forward(units)
        t.right(angles)

    turtle.done()

side = int(input("Enter the number of sides: "))  # Corrected input message
ang = int_ang(side)
units = int(input("Enter the number of units by which you want to draw the line: "))

draw_gon(side, units, ang)
