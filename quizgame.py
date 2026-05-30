def run_quiz():
    score = 0

    quiz = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "What is the largest mammal?": "Blue Whale",
        "What is the chemical symbol for water?": "H2O",
        "Who wrote To Kill a Mockingbird?": "Harper Lee"
    }

    question_number = 1

    print("\n===== QUIZ APP =====")

    for question, answer in quiz.items():
        print(f"\nQuestion {question_number}")
        user_answer = input(question + " : ")

        if user_answer.strip().lower() == answer.lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is: {answer}")

        question_number += 1

    total_questions = len(quiz)
    percentage = (score / total_questions) * 100

    print("\n===== RESULTS =====")
    print(f"Score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage == 100:
        print("🏆 Perfect Score!")
    elif percentage >= 80:
        print("🌟 Excellent!")
    elif percentage >= 60:
        print("👍 Good Job!")
    elif percentage >= 40:
        print("📚 Keep Practicing!")
    else:
        print("💪 Don't Give Up!")


while True:
    run_quiz()

    play_again = input("\nDo you want to play again? (y/n): ")

    if play_again.lower() != "y":
        print("Thanks for playing!")
        break
