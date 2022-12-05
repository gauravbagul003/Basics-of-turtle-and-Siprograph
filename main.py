import turtle as t

#for Drawing Square
# timmy_the_turtle = t.Turtle()
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

# To Draw Dash Line
# tim = t.Turtle()
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# To draw different shapes
# import random
# tim = t.Turtle()
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# To generate a random walk
# import random
# tim = t.Turtle()
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# To draw a siprograph
# import random
# tim = t.Turtle()
# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
# draw_spirograph(5)


