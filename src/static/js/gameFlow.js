$(document).ready(function() {
    let questionData;

    function displayQuestion(question) {
        questionData = question;
        console.log(questionData);

        $('#question').text(question.QuestionText);

        let optionsDiv = $('#options');
        optionsDiv.empty();

        /*        $.each(question.options, function(index, option) {
                    let button = $('<button class="btn btn-light">').text(option);
                    button.click(function() {
                        checkAnswer(index);
                    });
                    optionsDiv.append(button);
                });*/

        $.each(question.Answers, function(index, option) {
            let button = $('<button class="btn btn-light w-100 option-button">').text(option.AnswerText);
            button.click(function() {
                checkAnswer(option.Correct);
            });

            let colDiv = $('<div class="col-xl-6 col-lg-12">');
            colDiv.append(button);

            optionsDiv.append(colDiv);
        });

    }

    function getQuestion(){
        $.get('/_get_question', function(question) {
            if (!question.end) {
                displayQuestion(question);
            } else {
                window.location = root_url + "score";
            }
        });
    }

    function checkAnswer(selectedOption) {
        console.log(selectedOption)
        $.post(root_url + "_check_answer/" + selectedOption, function(data) {
            console.log(selectedOption);
        });
        getQuestion();
    }

    // Load the first question
    getQuestion();
});

