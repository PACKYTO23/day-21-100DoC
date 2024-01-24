# / # / # PROJECT OF DAY 20/21 # / # / #

# class Animal:  # # # Class Inheritance
#     def __init__(self):
#         self.num_eyes = 2

#     def breathe(self):
#         print("Inhale, exhale.")


# class Fish(Animal):
#     def __init__(self):
#         super().__init__()

#     def breathe(self):
#         super().breathe()
#         print("Doing this underwater.")

#     def swim(self):
#         print("Moving in water.")


# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:  # Detect collision with food.
        food.refresh()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:  # Detect collision with wall.
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
