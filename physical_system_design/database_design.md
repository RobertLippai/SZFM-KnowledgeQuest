# Adatbázisterv    

     @startuml
     entity Quiz {
        * QuizID : integer(3) <<PK>>
        --
        * PlayerName : char(10)
        * Score : integer(3)
        * Topic : char(10)
     }

     entity Topic {
        * TopicName : char(10) <<PK>>
        --
        Question : integer(3) <<FK>>
     }

     entity Question {
        * QuestionID : integer(3) <<PK>>
        --
        QuestionText : char(50)
        AnswerID : integer(3) <<FK>>
     }

     entity Question_Answer_KT {
        * QuestionID : integer(3) <<PK>>
        * AnswerID : integer(3) <<PK>>
        --
     }

     entity Answer {
        * AnswerID : integer(3) <<PK>>
        --
        Correct : boolean
        AnswerText : char(50)
     }

     Quiz ||--|| Topic
     Topic ||--o{ Question
     Question ||--o{ Question_Answer_KT
     Question_Answer_KT }o--|| Answer
     @enduml