from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Models the initial body of the scoreboard."""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Creates the game's scoreboard."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the scoreboard's score."""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """Ends and stops the game."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
