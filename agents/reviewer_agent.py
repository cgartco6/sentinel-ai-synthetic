class ReviewerAgent:
    def __init__(self):
        self.cycles = 0

    def review(self, task):
        self.cycles += 1
        return []

    def is_stable(self):
        return self.cycles > 3
