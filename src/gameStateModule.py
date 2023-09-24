from scoreManagerModule import ScoreManager
from timerModule import TimerManger


class GameState:
    def __init__(self, player_name, topic):
        self.player_name = player_name
        self.topic = topic
        self.questions_asked = set()
        self.number_of_asked_questions = 0
        self.score_manager = ScoreManager()
        self.timer = TimerManger(60)
        self.is_started = False

    def start_game(self):
        self.is_started = True

    def get_player_name(self):
        return self.player_name

    def get_topic(self):
        return self.topic

    def get_questions_asked(self):
        return self.questions_asked

    def get_number_of_asked_questions(self):
        return self.number_of_asked_questions

    def get_score(self):
        return self.score_manager.get_score()

    def get_time_left(self):
        return self.timer.get_time_left()

    def increment_score(self):
        self.score_manager.increment_score()

    def add_asked_question(self, question):
        self.questions_asked.add(question)

    def reset_game(self):
        self.questions_asked.clear()
        self.number_of_asked_questions = 0
        self.score_manager.reset_score()
        self.timer.reset()
        self.player_name = None
        self.topic = None
        self.is_started = False

    def __str__(self):
        return f'Player Name: {self.player_name}, Topic: {self.topic}, Questions Asked: {self.number_of_asked_questions}, Score: {self.get_score()}, Timer: {self.get_time_left()}'

