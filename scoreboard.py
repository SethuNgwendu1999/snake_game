from turtle import Turtle

ALIGNMENT = "center"
FONT = "Ariel", 17, "bold"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.high_score = 0
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.count}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def check(self):
        self.count += 1
        self.clear()
        self.write(f"Score: {self.count}", move=False, align="center", font=("Ariel", 17, "bold"))

    def reset(self):
        if self.count > self.high_score:
            self.high_score = self.count

    # def game_over(self):
    #     self.color("white")
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=("Ariel", 17, "bold"))


