from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt", mode="r") as file:
            self.High_Score = int(file.read())
        self.current_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.Update_score()


    def Update_score(self):
        self.goto(x=0, y=360)
        self.clear()
        self.write(f"Score: {self.current_score}   High Score: {self.High_Score}",
                   align="center", font=("Arial", 20, "normal"))

    def check_high_score(self):
        if self.current_score >= self.High_Score:
            self.High_Score = self.current_score
            with open("high_score.txt", "w") as file:
                file.write(str(self.High_Score))
        self.current_score = 0
        self.Update_score()

    def point(self):
        self.current_score += 1
        self.Update_score()

