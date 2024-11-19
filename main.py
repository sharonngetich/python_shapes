import turtle as t
import random

timmy = t.Turtle()
colours =["CornflowerBlue","DarkOrchid","IndianRed", "DeepSkyBlue","LightSwaGreen","Wheat","SlateGray","SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3, 11):
    timmy.color(random.choice(colours))
    draw_shape(shape_side_n)


