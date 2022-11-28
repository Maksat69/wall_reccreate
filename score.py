from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 80, "normal")


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(position)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"{self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

