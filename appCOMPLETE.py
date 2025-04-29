import json
mode = input("What mode: ").lower() #teacher or student

score = 0
streak = 0

class flashcards:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def display_info(self):
        return f"{self.question} {self.answer}"
        
    def to_dict(self):
        return {"question": self.question, "answer": self.answer}

if mode == "teacher":
    try:
        with open("flash.json", "r") as file:
            flash_data = json.load(file)
    except FileNotFoundError:
        flash_data = []
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        flash_data = []
    
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    new_card = flashcards(question, answer)
    flash_data.append(new_card.to_dict())
    
    with open("flash.json", "w") as file:
        json.dump(flash_data, file, indent=4)
    #appending flashcard dictionary to list in json
    print("flashcard added")
    print(new_card.display_info()) 

    print("Loaded flashcards:", flash_data)

elif mode == "student":
    try:
        with open("flash.json", "r") as file:
            flash_data = json.load(file)
    except FileNotFoundError:
        print("no flashcards found")
        exit()
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("no flashcards found")
        exit()

    z = "yes"
    while z.lower() == "yes":
        for card in flash_data:
            print(card["question"])
            y = input("What is the answer? ")

            if y.strip().lower() == card["answer"].strip().lower():
                print(f"Correct! The answer is: {card['answer']}")
                score += 1
                streak += 1
                print(f"streak: {streak}")
                print(f"score: {score}")
                z = input("continue? ")
                if streak >= 3:
                    score += 2
            else:
                print(f"Wrong. The correct answer is: {card['answer']}")
                streak = 0
                print(f"score: {score}")
                print(f"streak: {streak}")
                z = input("continue? ")
                if streak >= 3:
                    score += 2
  
   
        z = input("Do you want to go through the flashcards again? (yes/no): ")

    print("ok bye!:)")
    

else: 
    print("Invalid mode. Please choose 'teacher' or 'student'.")