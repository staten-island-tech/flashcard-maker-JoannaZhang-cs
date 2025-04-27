import json

input = input("What mode: ").lower #teacher or student
points = 0
streak = 0

class flashcards:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def to_dict(self):
            return {"question": self.question, "answer": self.answer}

mode = input("What mode?").lower()
if mode == "teacher":
    #teacher_mode()
    flash = flashcards(input("enter question: "), input("enter answer: "))
    try:
        with open("flash.json", "r") as file:
            flash_data = json.load(file)
    except FileNotFoundError:
        flash_data = []
    flash_data.append(flash.to_dict())

    with open("flash.json", "w") as file:
        json.dump(flash_data, file, indent=4)

elif mode == "student":
    #student_mode()
    with open("./flash.json", "w") as Flashcard:
        data = json.load(Flashcard)

    z = input("continue? ").lower()
    while z == "yes":
        for i in data:
            print(i["question"])
            y = input("what is the answer? ")
            if y == i["answer"]:
                print(f"The answer is {i['answer']}")
                print("correct")
                points += 1
                streak += 1
                print(f"streak: {streak}")
                print(f"points: {points}")
                z = input("continue? ")
                if streak >= 3:
                    points += 1
            else:
                print(i["answer"])
                streak = 0
                print("wrong")
                print(f"points: {points}")
                print(f"streak: {streak}")
                z = input("continue? ")
            if z == "no":
                break

else: 
    print("Invalid mode. Please choose 'teacher' or 'student'.")
