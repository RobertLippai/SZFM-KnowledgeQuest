from flask import Flask, render_template, jsonify, request, redirect

from gameStateModule import *
from questionBankModule import *

app = Flask(__name__)

current_question_index = 0  # Initialize current question index
question_bank = QuestionBank('test_questions.json')

current_game = None


@app.route("/", methods=["GET", "POST"])
def title_screen():
    global question_bank, current_game

    current_game = None
    # new game begins here
    # timer, score, questionBank gets reset everytime
    # current_game.reset_game()
    # question_bank.reset_used_questions()

    topics_list = []
    if request.method == "POST":
        player_name = request.form.get("nameOfPlayer")
        topic_name = request.form.get("nameOfTopic")
        current_game = GameState(player_name, topic_name)
        return redirect("/game")

    if request.method == "GET":
        topics_list = question_bank.get_topics()
    return render_template("titleScreen.html", topics_list=topics_list)


@app.route("/score")
def display_score():
    global score
    if current_game is None:
        return redirect("/")
    return render_template("gameEnd.html", score=current_game.score_manager.get_score())


@app.route("/game", methods=["GET"])
def game_menu():
    if current_game is None:
        return redirect("/")
    # main game logics
    return render_template("gamePlay.html")


@app.route("/_timer", methods=["GET", "POST"])
def timer():
    # timer background job
    # if the timer is up do something!!
    new_time = current_game.timer.decrement()

    return jsonify({"result": new_time})


@app.route('/get_question', methods=['GET'])
def get_question():
    global current_question_index
    global question_bank

    new_question = None

    try:
        new_question = question_bank.get_random_question()
    except ValueError:
        new_question = {'end': True}

    return jsonify(new_question)


@app.route("/check_answer/<int:selected_option>/<int:correct_option>", methods=['POST'])
def check_answer(selected_option, correct_option):
    global score

    if selected_option == correct_option:
        result = "Correct!"
        current_game.score_manager.increment_score()
    else:
        result = "Incorrect :("
    return jsonify({'result': result})


if __name__ == "__main__":
    app.run()
