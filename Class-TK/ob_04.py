class Course:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def avg(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

    def info(self):
        return f"과목: {self.name}, 평균: {self.avg():.1f}"

c = Course("파이썬")
c.add_score(80)
c.add_score(90)
print(c.info()) #과목:파이썬, 평균:85.0