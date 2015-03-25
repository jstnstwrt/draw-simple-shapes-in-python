import turtle 

def draw_square():
	window = turtle.Screen()
	turt = turtle.Turtle()
	turt.shape("turtle")
	turt.color("yellow")
	i = 0
	while i <= 4:
		turt.forward(100)
		turt.right(90)
		i += 1

draw_square()