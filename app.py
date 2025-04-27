""" """ """ class Calculator():
    def add(x,y):
        print(x+y)
        return x + y
    def add_many(list):
        print(sum(list))
        return sum(list)
    def subtract(list):
        return list
Calculator.add()
dict.values """

""" class User:
    def __init__(self, id, name)
    super(). __init__(id, name) """
""" /* 
class Merchant:
    def  __init__(self, name, products):
    #defines look of class
        self.name = name
        self.products = products
    def sell(self, item):
        self.products.remove(item)
        print(self.products)
Joanna = Merchant ("Joanna", ['Chicken', 'Pork', 'Beef'])
Joanna.sell('Pork')

Alvin = Merchant ("Alvin", ["Human", "Alvin's Servitude", "Breaks", "Organs"])
Alvin.sell("Human")
 */


class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def create_dict(self):
        x = {self.name : self.age}
        return x
Whalen = Teacher("Whalen", 35) 
print(Whalen.create_dict())

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def create_dict(self):
        x = {self.name : self.age}
        return x
Whalen = Teacher("Whalen", 35) 
print(Whalen.create_dict())

/* 
Teacher Mode

In teacher mode you will be asking the user to input a word/phrase and the
answer as a key:value pair. These pairs will be written to a json file called
FlashCards.json

Student Mode
In student mode you will present the student with the
phrases/words/images and the user will type the answer in the terminal.
Keep a tally of correct answers and provide a score. Give students bonus
points for “Streaks” */ """





import json
mode = input("What mode: ").lower() #teacher or student


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
    
    x = flashcards("Kublai", "Grandson of Genghis")
    #everything above is called "Class"
    flash_data.append(x.to_dict())
    with open("flash.json", "w") as file:
        json.dump(flash_data, file, indent=4)
    #appending flashcard dictionary to list in json
    print(x.display_info()) 


elif mode == "student":
    try:
        with open("flash.json", "r") as Flashcard:
            data = json.load(Flashcard)
    except FileNotFoundError:
        print("No flashcards found.")
        exit()

    z = "yes"
    while z.lower() == "yes":
        for i in data:
            print(i["question"])
            y = input("What is the answer? ")

            if y.strip().lower() == i["answer"].strip().lower():
                print(f"Correct! The answer is: {i['answer']}")
            else:
                print(f"Wrong. The correct answer is: {i['answer']}")

        #z = input("Continue? (yes/no): ")

else: 
    print("Invalid mode. Please choose 'teacher' or 'student'.")








""" if user_answer.lower() == correct_answer.lower():
            streak += 1
            bonus = 2 if streak >= 3 else 0
            gained = 1 + bonus
            print(f"✅ Correct! +{gained} points (Streak: {streak})")
            score += gained
        else:
            print(f"❌ Wrong. Correct answer was: '{correct_answer}'")
            streak = 0

        print(f"Current Score: {score}\n") """




""" def teacher_mode():
    print("Entering teacher Mode. Type 'exit' as the question to stop.")
    flashcards = load_flashcards()
    #flashcards = {}
    while True:
        question = input("Enter a word/phrase (or type 'exit' to stop): ").strip()
        if question.lower() == 'exit':
            break
        answer = input(f"Enter the answer for '{question}': ").strip()
        flashcards[question] = answer
        print(f"Added: '{question}' -> '{answer}'\n") """

  

    #while loop to print out this flashcard on loop until student types answer?

        
      

""" def student_mode():
        print("Entering student mode. Type 'exit' to stop.")
        flashcards = load_flashcards()
        if not flashcards:
            print("No flashcards available. Please add some in teacher mode.")
            return

        score = 0
        streak = 0
        items = [(item["question"], item["answer"]) for item in flash_data]
       
        for question, correct_answer in items:
            user_answer = input(f"What is the answer to: '{question}'? ").strip()
            if user_answer.lower() == 'exit':
                break """






#just get it done
#use classes for individual flashcards if necessary
















""" 

class Teacher:

print ("input a word/phrase:")

flashcards = word("Toyota", "Camry", 2023, "camry_image.jpg")
print(flashcards.display_info())  # Output: 2023 Toyota Camry

cars = [
    Car("Toyota", "Camry", 2023, "camry_image.jpg"),
    Car("Honda", "Civic", 2022, "civic_image.jpg"),
    Car("Ford", "Mustang", 2021, "mustang_image.jpg")
]

# Convert objects to dictionaries
cars_data = [car.to_dict() for car in cars]

# Save to a JSON file
with open("cars.json", "w") as file:
    json.dump(cars_data, file, indent=4)

    new_car = Car("Chevrolet", "Malibu", 2024, "malibu_image.jpg")

# Load existing data
try:
    with open("cars.json", "r") as file:
        cars_data = json.load(file)
except FileNotFoundError:
    cars_data = []

# Append new car
cars_data.append(new_car.to_dict())

# Save updated data back to file
with open("cars.json", "w") as file:
    json.dump(cars_data, file, indent=4) """