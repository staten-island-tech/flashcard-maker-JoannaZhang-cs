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



class Teacher:

print input("input a word/phrase:")

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
    json.dump(cars_data, file, indent=4)