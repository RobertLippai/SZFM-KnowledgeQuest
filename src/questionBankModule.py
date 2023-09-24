import json
import random


class QuestionBank:
    def __init__(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            self.questions = json.load(file)
        self.used_questions = set()

    # random question from any topics
    def get_random_question(self):
        if len(self.used_questions) == len(self.questions):
            raise ValueError("All questions have been used.")

        available_questions = [q for q in self.questions if q['question'] not in self.used_questions]
        random_question = random.choice(available_questions)
        self.used_questions.add(random_question['question'])
        print(random_question)
        return random_question

    # random question from a given topics
    def get_random_question_topics(self, json_file, topics_name):
        with open(json_file, encoding="utf-8") as f:
            topics = json.load(f).get("Topics")

            if topics_name not in [topic.get("TopicName") for topic in topics]:
                raise ValueError("Invalid topic name.")

            for topic in topics:
                if topic.get("TopicName") == topics_name:
                    questions = topic.get("Questions")
                    break
        random.shuffle(questions)
        return questions.pop()

    # returns all the avaible topics
    def get_topics(self, json_file):
        with open(json_file, encoding="utf-8") as f:
            topics = json.load(f).get("Topics")

        return [topic.get("TopicName") for topic in topics]

    # resets the used question set
    def reset_used_questions(self):
        self.used_questions.clear()

if __name__ == "__main__":
    question_bank = QuestionBank('test_questions.json')
    print(question_bank.get_topics("static/questions.json"))
    print(question_bank.get_random_question())
    print(question_bank.get_random_question_topics("static/questions.json", "Állatok"))
