import app

def test_title_screen():
    # Test if the title screen loaded successfully
    client = app.app.test_client()

    response = client.get('/')

    assert response.status_code == 200
    assert b"<title>Knowledge Quest</title>" in response.data


def test_unstarted_game_redirection():
    # If the game has not been started
    # the player shouldn't be able to access the score or the game page, so
    # they will get redirected to the title screen
    client = app.app.test_client()

    response = client.get('/score')
    assert response.status_code == 302

    response = client.get('/game')
    assert response.status_code == 302


def test_game_setup():
    client = app.app.test_client()
    data = {
        'nameOfPlayer': 'Teszt Játékos',
        'nameOfTopic': 'Állatok'
    }
    response = client.post('/', data=data, follow_redirects=True)

    assert response.status_code == 200

    assert 'Teszt Játékos' == app.current_game.get_player_name()
    assert 'Állatok' == app.current_game.get_topic()


def test_check_answer():
    client = app.app.test_client()

    response = client.post('/_check_answer/true')

    assert response.status_code == 200
    assert b'Correct!' in response.data

    response = client.post('/_check_answer/false')

    assert response.status_code == 200
    assert b'Incorrect :(' in response.data


def test_timer_backend():
    # First we get the remaining time, it should be the same as in the current_game.get_time_left() function

    client = app.app.test_client()

    response = client.get('/_timer')

    assert response.status_code == 200
    assert str(app.current_game.get_time_left()) in response.data.decode('utf-8')

    print(response.data)
    assert response.status_code == 200
    assert str(app.current_game.get_time_left()) in response.data.decode('utf-8')


def test_get_question():
    client = app.app.test_client()
    data = {
        'nameOfPlayer': 'Test',
        'nameOfTopic': 'Állatok'
    }
    client.post('/', data=data, follow_redirects=True)

    response = client.get('/_get_question')
    print(response.data)
    assert response.status_code == 200
    assert b'Answers' in response.data
