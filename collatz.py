import turtle as t

t.bgcolor("black")
t.color("red")
t.hideturtle()

for index, n in enumerate(range(1, 25)):
    sequence = []
    while n > 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    print(f"Sequence {index + 1} completed: {sequence}")

    sequence.reverse()

    t.goto(0, 0)
    t.setheading(90)
    for i in sequence:
        t.pendown()
        if i % 2 == 0:
            t.right(15)
            t.forward(30)
        else:
            t.left(15)
            t.forward(30)
        t.penup()

t.done()