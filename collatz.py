import turtle as t
from random import randint

# Turtle setup
screen = t.Screen()
screen.setworldcoordinates(-10000, -10000, 10000, 10000)

t.bgcolor("black")
t.color("red")
t.hideturtle()
t.speed(0)
t.tracer(20000, 0)

max_steps = 0

sequence_cache = {}

# Main loop
for index, n in enumerate(range(1, 5000)):
    sequence = []

    # Collatz loop
    while n > 1:
        if n in sequence_cache:
            sequence.extend(sequence_cache[n])
            break
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    else:
        sequence.append(1)

    for i, val in enumerate(sequence):
        if val not in sequence_cache:
            sequence_cache[val] = sequence[i:]

    if len(sequence) > max_steps:
        max_steps = len(sequence)

    sequence.reverse()
    
    t.goto(0, -8000)
    t.setheading(90)

    seen = {}

    # Draw values in sequence loop
    for i in sequence:
        if i in seen:
            x, y, heading = seen[i]
            t.penup()
            t.goto(x, y)
            t.setheading(heading)
        else:
            t.pendown()
            if i % 2 == 0:
                t.right(5)
            else:
                t.left(9)
            t.forward(75)
            t.penup()
            
            seen[i] = (t.xcor(), t.ycor(), t.heading())

print(f"Highest number of steps reached: {max_steps}")

t.update()
t.done()