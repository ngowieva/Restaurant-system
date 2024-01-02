def run_quiz(questions):
    score = 0
    for question in questions:
        print(question['question'])
        for i, option in enumerate(question['options'], 1):
            print(f"{i}. {option}")

        user_answer = int(input("Your answer (enter the corresponding number): "))
        correct_answer = question['correct_option']

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 5
        else:
            print(f"Wrong! The correct answer is {correct_answer}: {question['options'][correct_answer - 1]}\n")

    print(f"Your final score is: {score}/{len(questions)}")


# Example questions
quiz_questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Berlin', 'Paris', 'London', 'Rome'],
        'correct_option': 2
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Jupiter', 'Venus', 'Saturn'],
        'correct_option': 1
    },
    {
        'question': 'what is the long form of CPU? ',
        'options': ['center process unty','central processing unity','center processor unity'],
        'correct_option':2
    },
    {
        'question': 'what is RAM ?',
        'options':['Read analogy Memory','Ready Access Memory','Random Access Memory'],
        'correct_option':3
    }
]

# Run the quiz
run_quiz(quiz_questions)
