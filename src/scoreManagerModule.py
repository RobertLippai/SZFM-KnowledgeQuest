class ScoreManager:
    def __init__(self):
        self.score = 0  # Set the initial score

    def increment_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def reset_score(self):
        self.score = 0  # Reset the score to its initial value
