from turtle import Turtle, Screen

with open("data.txt") as hs:
    hs_int = int(hs.read())

ALIGN = "center"
FONT = ("System", 10, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.h_score = hs_int
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(x=0, y=280)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.h_score}", font=FONT, align=ALIGN)

    def sb_reset(self):
        if self.score > self.h_score:
            self.h_score = self.score
            with open("data.txt", mode="w") as old_hs:
                old_hs.write(f"{self.h_score}")
        self.score = 0
        self.score_update()

    def sb_refresh(self):
        self.score += 1
        self.score_update()
