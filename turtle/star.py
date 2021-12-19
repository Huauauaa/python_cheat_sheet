import turtle
from turtle import *

color('red', 'yellow')
turtle.speed('fast')
# tracer(False)

begin_fill()


for i in range(5):
    forward(200)
    right(180 - 36)
end_fill()
penup()
goto(-200, 0)
pendown()

begin_fill()
width = 80
for i in range(5):
    forward(width)
    right(180 - 36)
    forward(width)
    left(36 + 36)

penup()
end_fill()
done()
