import json
import os
import random

flash.json = 'flash.json'

def load_flashcards():
    if os.path.exists(flash.json):
        with open(flash.json, 'r') as f:
            return json.load(f)
    return {}

def save_flashcards(flashcards):
    with open(flash.json, 'w') as f:
        json.dump(flashcards, f, indent=4)

def teacher_mode():
    print("Entering Teacher Mode. Type 'exit' as the question to stop.")
    flashcards = load_flashcards()

    while True:
        question = input("Enter a word/phrase (or type 'exit' to stop): ").strip()
        if question.lower() == 'exit':
            break
        answer = input(f"Enter the answer for '{question}': ").strip()
        flashcards[question] = answer
        print(f"Added: '{question}' -> '{answer}'\n")

    save_flashcards(flashcards)
    print("Flashcards saved!")

def student_mode():
    flashcards = load_flashcards()
    if not flashcards:
        print("No flashcards found. Add some in Teacher Mode first.")
        return

    items = list(flashcards.items())
    random.shuffle(items)

    score = 0
    streak = 0
    print("Starting quiz! Type 'exit' to stop.\n")

    for question, correct_answer in items:
        user_answer = input(f"What is the answer to: '{question}'? ").strip()
        if user_answer.lower() == 'exit':
            break

        if user_answer.lower() == correct_answer.lower():
            streak += 1
            bonus = 2 if streak >= 3 else 0
            gained = 1 + bonus
            print(f"✅ Correct! +{gained} points (Streak: {streak})")
            score += gained
        else:
            print(f"❌ Wrong. Correct answer was: '{correct_answer}'")
            streak = 0

        print(f"Current Score: {score}\n")

    print(f"Final Score: {score} 🎉")

def main():
    print("Welcome to Flashcards!")
    mode = input("Choose mode (teacher/student): ").strip().lower()

    if mode == 'teacher':
        teacher_mode()
    elif mode == 'student':
        student_mode()
    else:
        print("Invalid mode. Please restart and choose 'teacher' or 'student'.")

if __name__ == "__main__":
    main()