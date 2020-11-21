from turtle import Turtle, Screen


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(x=0, y=280)
        self.write(f"Score: {self.score}", font=("System", 10, "bold"), align="center")


    def sb_refresh(self):
        self.clear()
        self.score += 1
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(x=0, y=280)
        self.write(f"Score: {self.score}", font=("Arial", 12, "bold"), align="center")
