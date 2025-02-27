import turtle

def draw_yang(y_pos, is_moving):
    turtle.width(3)
    turtle.penup()
    turtle.goto(-50, y_pos)
    turtle.pendown()
    turtle.setheading(0)  # Face east
    turtle.forward(100)  # Draw unbroken line
    if is_moving:
        # Draw X
        turtle.penup()
        turtle.goto(-15, y_pos + 15)
        turtle.pendown()
        turtle.goto(15, y_pos - 15)
        turtle.penup()
        turtle.goto(-15, y_pos - 15)
        turtle.pendown()
        turtle.goto(15, y_pos + 15)
        turtle.penup()

def draw_yin(y_pos, is_moving):
    turtle.penup()
    turtle.goto(-50, y_pos)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(40)  # Left segment
    turtle.penup()
    turtle.goto(10, y_pos)
    turtle.pendown()
    turtle.forward(40)  # Right segment
    turtle.penup()
    if is_moving:
        # Draw circle in the gap
        turtle.goto(0, y_pos - 8)
        turtle.pendown()
        turtle.circle(8)
        turtle.penup()

def draw_hexagram(numbers):
    if len(numbers) != 6:
        raise ValueError("Input list must have exactly 6 numbers.")
    valid_numbers = {6, 7, 8, 9}
    if not all(num in valid_numbers for num in numbers):
        raise ValueError("Numbers must be 6, 7, 8, or 9.")
    
    turtle.speed(0)  # Fastest drawing
    turtle.hideturtle()
    screen = turtle.Screen()
    screen.setup(width=400, height=600)
    screen.setworldcoordinates(-60, -20, 60, 220)  # Adjust view window
    
    for i in range(6):
        num = numbers[i]
        y_pos = i * 40  # Vertical position from bottom (0) to top (200)
        if num == 7:
            draw_yang(y_pos, False)
        elif num == 8:
            draw_yin(y_pos, False)
        elif num == 6:
            draw_yang(y_pos, True)
        elif num == 9:
            draw_yin(y_pos, True)
    
    turtle.done()

# Example usage:
input_numbers = [6,7,7,7,7,8]  # Test input
draw_hexagram(input_numbers)
turtle.hideturtle()