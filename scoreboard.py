from turtle import Turtle, Screen

ALIGN = "center"
FONT = ("System", 10, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(x=0, y=280)
        self.score_update()

    def score_update(self):
        self.write(f"Score: {self.score}", font=FONT, align=ALIGN)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def sb_refresh(self):
        self.clear()
        self.score += 1
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(x=0, y=280)
        self.score_update()
