from flask import Flask, render_template, jsonify, request, redirect

import question_handler
from gameStateModule import *
from questionBankModule import *
from question_handler import *

app = Flask(__name__)

question_bank = QuestionBank('test_questions.json')
current_game = GameState(None, None)
questions = None

# FIXED
# firefox bugged font rendering (áéíő)
# if questions run out the game cant be restarted

@app.route("/", methods=["GET", "POST"])
def title_screen():
    global question_bank, current_game, questions

    # When this screen is accessed a new game begins.
    # The gameState, questionBank gets reset
    current_game.reset_game()
    question_bank.reset_used_questions()

    if request.method == "POST":
        player_name = request.form.get("nameOfPlayer")
        topic_name = request.form.get("nameOfTopic")
        questions = choose_topic(topic_name)

        current_game = GameState(player_name, topic_name)
        current_game.start_game()
        return redirect("/game")

    if request.method == "GET":
        topics_list = []
        topics_list = question_handler.get_topic_names()
        return render_template("titleScreen.html", topics_list=topics_list)


@app.route("/score")
def score_screen():
    global current_game, questions

    if current_game.is_started is False:
        return redirect("/")

    result = {}
    result["PlayerName"] = current_game.get_player_name()
    score = current_game.score_manager.get_score()
    asked = current_game.get_number_of_asked_questions()
    result["Topic"] = current_game.get_topic()
    result["Date"] = get_current_date()

    result["Score"] = (score/asked)*100
    # save the results
    save_result(result)

    # Kinyerjük az első 5 embert a get_high_scores függvénnyel
    high_scores = get_high_scores()
    while len(high_scores) < 5:
        high_scores.append({
            "PlayerName": "-",
            "Score": 0,
            "Topic": "-",
            "Date": "0000.00.00. 00:00:00"
        })

    print("Printing game info: " + str(current_game))

    number_of_asked_question = current_game.get_number_of_asked_questions()

    return render_template("gameEnd.html", score=current_game.score_manager.get_score(), high_scores=high_scores, number_of_asked_question=number_of_asked_question)



@app.route("/game", methods=["GET"])
def gameplay_screen():
    global current_game

    if current_game.is_started is False:
        return redirect("/")

    # actual gameplay
    return render_template("gamePlay.html")


# accessed via jQuery request
@app.route("/_timer", methods=["GET", "POST"])
def timer_update():
    global current_game

    if request.method == "POST":
        # timer background job
        new_time = current_game.timer.decrement()

        return jsonify({"result": new_time})

    if request.method == "GET":
        # get time left
        time_left = current_game.timer.get_time_left()

        return jsonify({"result": time_left})


@app.route('/_get_question', methods=['GET'])
def get_question():
    global question_bank, current_game, questions

    try:
        new_question = choose_question(questions)
        print(new_question)
        # new_question = question_bank.get_random_question()
        current_game.number_of_asked_questions += 1
    except IndexError:
        new_question = {'end': True}

    return jsonify(new_question)


#@app.route("/_check_answer/<int:selected_option>/<int:correct_option>", methods=['POST'])
#def check_answer(selected_option, correct_option):
#    global current_game

#    if selected_option == correct_option:
#        result = "Correct!"
#        current_game.score_manager.increment_score()
 #   else:
 #       result = "Incorrect :("

 #   return jsonify({'result': result})

@app.route("/_check_answer/<string:is_correct>", methods=['POST'])
def check_answer(is_correct):
    global current_game

    print(is_correct)

    if is_correct == "true":
        result = "Correct!"
        current_game.score_manager.increment_score()
    else:
        result = "Incorrect :("

    print(result)
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run()
