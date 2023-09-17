## Osztályterv

![Osztályterv](img/class_diagram.png)

### GameState

- topic: az adott játék kérdéseinek témája
- question_asked: a már feltett kérdések
- score_manager: a pontozásért felelős adattag
- timer: az időzítésért felelős adattag
---
- increment_score(): növeli a megszerezett pontszámot
- add_question(): eltárolja a feltett kérdést
- reset_game(): újraindítja a játékot

### TimerManager

- current_time: a hátralévő idő
---
- decrement(): a számlálót csökkenti
- reset(): visszaállítja a számlálót

### ScoreManager

- score: a pontszám, intként tárolva
---
- increment_score(): a pontszám növeléséért felelős metódus
- reset_score(): a pontszám visszaállítása

### QuestionBank

- used_questions: a már feltett kérdések halmaza
---
- get_random_question(): egy véletlen, még nem választott kérdéssel tér vissza
- reset_used_questions(): visszaállítja a már használt kérdéseket
---
```
@startuml
Class GameState {
 topic
 questions_asked
 score_manager
 timer
 --
 get_topic()
 get_question_asked()
 get_score()
 get_timer()
 increment_score()
 add_question()
 reset_game()
}

Class TimerManager {
 current_time
 --
 decrement()
 reset()
}

Class ScoreManager {
 score
 --
 increment_score()
 get_score()
 reset_score()
}

Class QuestionBank {
 used_questions
 get_random_question()
 reset_used_questions()
}
@enduml```