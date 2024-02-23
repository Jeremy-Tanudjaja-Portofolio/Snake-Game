from turtle import Turtle

class Score(Turtle):

    score = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-40, 260)
        self.pencolor("white")
        self.pendown()
        self.write(f"Score is: {self.score}", font = ("Arial", 20, "normal"))

    def update_score(self):
        self.clear()
        self.score = self.score + 1
        self.write(f"Score is: {self.score}", font = ("Arial", 20, "normal"))

    def game_over(self):
        self.penup()
        self.goto(-50,0)
        self.pendown()
        self.write(f"Game Over \nFinal Score is: {self.score}", font=("Arial", 20, "normal"))