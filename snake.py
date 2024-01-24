from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Models the initial body of the snake."""
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        """Creates segments of the snake's body."""
        for position in STARTING_POSITIONS:
            body = Turtle("square")
            body.color("white")
            body.penup()
            body.goto(position)
            self.snake_body.append(body)

    def move(self):
        """Moves the head and the body follows."""
        for num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[num - 1].xcor()
            new_y = self.snake_body[num - 1].ycor()
            self.snake_body[num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Moves the snake up."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Moves the snake down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Moves the snake left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Moves the snake right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
