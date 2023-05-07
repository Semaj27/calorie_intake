from dataclasses import dataclass

import numpy as np
import matplotlib as plt


CALORIE_GOAL_LIMIT = 3000   # kcal
PROTEIN_GOAL= 180   # grams
FAT_GOAL = 80   # grams
CARB_GOAL = 300   # grams

today = []

@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int


done = False

while not done:
    print(""" 
    (1) Add a new food 
    (2) Visualize progress
    (q) Quit
    """)

    choice = input("Choose an option: ")

    if choice == "1":
        print("Adding a new food!")
        name = input("Name: ")
        calories = int(input("Calories: "))
        protien = int(input("Proteins: "))
        fats = int(input("Fats: "))
        carbs = int(input("Carbs: "))
        food = Food(name, calories, protien, fats, carbs)
        today.append(food)
        print("Successfully added!")

    elif choice == "2":
        calories_sum = sum(food.calories for food in today)
        protien_sum = sum(food.protien for food in today)
        fats_sum = sum(food.fat for food in today)
        carbs_sum = sum(food.carbs for food in today)


        fig, axs = plt.subplots(2,2)
        axs[0, 0].pie([protien_sum, fats_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"], autopct = "%1.1f%%")
        axs[0, 0].set_title("Macronutrients Distribution")
        fig.tight_layout()
        plt.show