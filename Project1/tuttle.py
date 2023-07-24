import turtle 

t = turtle.Screen()
t.bgcolor('black')
turtle.color('white')
turtle.speed(60)



turtle.up()
turtle.sety(-300)
turtle.down()
a,b,c = 30,30,30
for i in range(1,115):
    a += 1
    b += 1
    c += 1
    if(a == 0):
        a = 0
        b = 0
        c = 0
    turtle.colormode(255)
    turtle.pencolor((a,b,c))
    turtle.circle(80,360)
    x = i*3
    turtle.up()
    turtle.right(5)
    turtle.seth(x)
    turtle.forward(15)
    turtle.down()


# SUN Cordinate
# turtle.ht()
# turtle.width(3)
# for i in range(1,38):
#     turtle.circle(50,-160)
#     turtle.left(250)
#     turtle.circle(50,140)
#     turtle.left(180)
#     turtle.circle(50,-140)
#     turtle.up()
#     turtle.home()
#     turtle.left(10*i)
#     turtle.down()


# RECTANGLE Shape
# a = 90
# y = 100
# for i in range(40):
#     turtle.forward(25*i//2)
#     turtle.right(a)
#     turtle.dot(8,'black')
#     #turtle.stamp()



turtle.done()