from turtle import Turtle
import random


class Food(Turtle):
    """Models the initial body of the food."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("red")
        self.speed(0)
        self.refresh()

    def refresh(self):
        """Creates the new coordinates for the food."""
        random_x = random.randint(-285, 285)
        random_y = random.randint(-285, 285)
        self.goto(random_x, random_y)
