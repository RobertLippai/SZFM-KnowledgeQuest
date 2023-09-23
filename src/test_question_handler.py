import pytest

from question_handler import (
    choose_question,
    choose_topic,
    get_answers,
    get_high_scores,
    get_questiontext,
    get_results,
    get_score_of_player,
    get_topic_names,
)

TEST_QUESTION = {
    "QuestionText": "Mikor végződött a második világháború?",
    "Answers": [
        {"AnswerText": "1945", "Correct": True},
        {"AnswerText": "1941", "Correct": False},
        {"AnswerText": "1939", "Correct": False},
        {"AnswerText": "1950", "Correct": False},
    ],
}

TEST_PLAYER_INFO = {
    "PlayerName": "B\u00e9la",
    "Score": 9,
    "Topic": "\u00c1llatok",
    "Date": "2023.09.23. 12:43:49",
}


def test_get_topic_names():
    result = get_topic_names()
    assert isinstance(result, list)
    for topic in result:
        assert isinstance(topic, str)
    assert len(result) == 5


def test_choose_topic():
    result = choose_topic("Történelem")
    assert isinstance(result, list)
    assert len(result) == 11


def test_choose_topic_exception():
    with pytest.raises(ValueError) as e:
        choose_topic("ASD")

    assert str(e.value) == "Invalid topic name."


def test_choose_question():
    questions = choose_topic("Történelem")
    init_size = len(questions)
    assert isinstance(choose_question(questions), dict)
    assert init_size != len(questions)


def test_choose_question_exception():
    with pytest.raises(IndexError):
        choose_question([])


def test_get_questiontext():
    assert get_questiontext(TEST_QUESTION) == "Mikor végződött a második világháború?"


def test_get_answers():
    assert get_answers(TEST_QUESTION) == [
        {"AnswerText": "1945", "Correct": True},
        {"AnswerText": "1941", "Correct": False},
        {"AnswerText": "1939", "Correct": False},
        {"AnswerText": "1950", "Correct": False},
    ]


def test_get_score_of_player():
    assert get_score_of_player(TEST_PLAYER_INFO) == 9


def test_get_results():
    results = get_results()
    assert isinstance(results, list)
    for result in results:
        assert isinstance(result, dict)


def test_get_high_scores():
    results = get_high_scores()
    assert isinstance(results, list)
    for result in results:
        assert isinstance(result, dict)
    assert len(results) <= 5
