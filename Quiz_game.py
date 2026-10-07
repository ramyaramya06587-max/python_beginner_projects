questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Bangalore", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "Which language are we learning?",
        "options": ["Java", "Python", "C++", "HTML"],
        "answer": "Python"
    },
    {
        "question": "How many days are there in a week?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    }
]

score = 0

for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    answer = input("Your answer: ")

    if answer.lower() == question["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nQuiz finished!")
print("Your score:", score, "/", len(questions))