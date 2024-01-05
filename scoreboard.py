from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-230, 270)
        self.update_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align="center", font=("Courier", 24, "normal"))
