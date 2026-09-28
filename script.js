function askQuestion() {
    let question = document.getElementById("question").value;
    let answer = document.getElementById("answer");

    if (question.trim() === "") {
        answer.innerHTML = "Please enter a question.";
        return;
    }

    if (question.toLowerCase().includes("largest ocean")) {
        answer.innerHTML =
            "<b>Answer:</b> The Pacific Ocean is the largest ocean on Earth.";
    } else {
        answer.innerHTML =
            "<b>EduGenie:</b> Your question is received. " +
            "AI-generated answers can be connected through the backend.";
    }
}


function generateQuiz() {
    let topic = document.getElementById("topic").value;
    let quiz = document.getElementById("quiz");

    if (topic.trim() === "") {
        quiz.innerHTML = "Please enter a topic.";
        return;
    }

    quiz.innerHTML =
        "<b>Quiz: " + topic + "</b><br><br>" +
        "1. What is the main idea of " + topic + "?<br>" +
        "A) Concept 1 &nbsp; B) Concept 2 &nbsp; C) Concept 3<br><br>" +
        "2. Which statement is related to " + topic + "?<br>" +
        "A) Option 1 &nbsp; B) Option 2 &nbsp; C) Option 3";
}


function generatePath() {
    let topic = document.getElementById("learningTopic").value;
    let path = document.getElementById("path");

    if (topic.trim() === "") {
        path.innerHTML = "Please enter a learning topic.";
        return;
    }

    path.innerHTML =
        "<b>Learning Path: " + topic + "</b><br><br>" +
        "1. Beginner: Learn basic concepts<br>" +
        "2. Intermediate: Practice examples<br>" +
        "3. Advanced: Work with real projects<br>" +
        "4. Practice: Solve exercises and quizzes<br>" +
        "5. Project: Build a small application";
}


function summarizeText() {
    let text = document.getElementById("text").value;
    let summary = document.getElementById("summary");

    if (text.trim() === "") {
        summary.innerHTML = "Please enter some text.";
        return;
    }

    let words = text.split(/\s+/);
    let shortText = words.slice(0, 35).join(" ");

    summary.innerHTML =
        "<b>Summary:</b> " + shortText +
        (words.length > 35 ? "..." : "");
}