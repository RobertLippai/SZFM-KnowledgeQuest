import json
import random
import sys
from datetime import datetime

CHOSEN_TOPIC = "Állatok"
PLAYER_NAME = "Béla"
SCORE = 9


def get_topic_names():
    with open("static/questions.json") as f:
        topics = json.load(f).get("Topics")

    return [topic.get("TopicName") for topic in topics]


def choose_topic(choice):
    """Returns every question for a given topic as a list, with answers included.

    Raises a ValueError if the topic name is not found."""
    with open("static/questions.json") as f:
        topics = json.load(f).get("Topics")

        if choice not in [topic.get("TopicName") for topic in topics]:
            raise ValueError("Invalid topic name.")

        for topic in topics:
            if topic.get("TopicName") == choice:
                questions = topic.get("Questions")
                break
    return questions


def choose_question(questions):
    """Returns a random question, and takes it out of the list of available questions."""
    if len(questions) == 0:
        raise IndexError("No more available questions in topic.")

    random.shuffle(questions)
    return questions.pop()


def get_questiontext(question):
    return question.get("QuestionText")


def get_answers(question):
    return question.get("Answers")


def get_score_of_player(e):
    return e.get("Score")


def get_current_date():
    now = datetime.now()
    dt_string = now.strftime("%Y.%m.%d. %H:%M:%S")
    return dt_string


def get_results():
    """Reads the results and returns them in a list, or an empty list if the file is empty/does not exist."""
    try:
        with open("results.json", "r") as f:
            results = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        results = []

    return results


def get_high_scores():
    """Reads the results, sorts them by score, and returns the first three elements of the list."""
    results = get_results()
    results.sort(reverse=True, key=get_score_of_player)
    return results[:5]


def save_result(result):
    """Reads the results, appends the current result to the list, and saves it back to the file."""
    results = get_results()
    results.append(result)
    try:
        with open("results.json", "w") as f:
            json.dump(results, f, indent=4)
    except:
        print("Unable to write to file.", file=sys.stderr)


def main():
    try:
        questions = choose_topic(CHOSEN_TOPIC)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    while True:
        try:
            question = choose_question(questions)
        except IndexError as e:
            print(f"Error: {e}", file=sys.stderr)
            break
        question_text = get_questiontext(question)
        answers = get_answers(question)
        print(question_text)
        for answer in answers:
            if answer.get("Correct"):
                print("!", end="")
            print(answer.get("AnswerText"), end=" ")
        inp = input("\n")
        if inp == "x":
            break

    result = {}
    result["PlayerName"] = PLAYER_NAME
    result["Score"] = SCORE
    result["Topic"] = CHOSEN_TOPIC
    result["Date"] = get_current_date()

    save_result(result)

    print(get_high_scores())

    print(get_topic_names())


if __name__ == "__main__":
    main()
