$(document).ready(function() {
    let questionData;

    function displayQuestion(question) {
        questionData = question;
        console.log(questionData);

        $('#question').text(question.question);

        let optionsDiv = $('#options');
        optionsDiv.empty();

        $.each(question.options, function(index, option) {
            let button = $('<button class="btn btn-light">').text(option);
            button.click(function() {
                checkAnswer(index);
            });
            optionsDiv.append(button);
        });
    }

    function getQuestion(){
        $.get('/get_question', function(question) {
            if (!question.end) {
                displayQuestion(question);
            } else {
                window.location = root_url + "score";
            }
        });
    }

    function checkAnswer(selectedOption) {
        $.post(root_url + "check_answer/" + selectedOption + "/" + questionData.correct_option, function(data) {
            console.log(selectedOption == questionData.correct_option);
        });
        getQuestion();
    }

    // Load the first question
    getQuestion();
});

