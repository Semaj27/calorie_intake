from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

# Set the backend to use for displaying graphs
plt.switch_backend('TkAgg')

CALORIE_GOAL_LIMIT = 1500   # kcal
PROTEIN_GOAL= 112   # grams
FAT_GOAL = 50   # grams
CARB_GOAL = 150   # grams

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
    (1) Add a new meal 
    (2) Visualize progress
    (q) Quit
    """)

    choice = input("Choose an option: ")

    if choice == "1":
        print("Adding a new meal!")
        name = input("Name: ")
        calories = int(input("Calories: "))
        protien = int(input("Proteins: "))
        fats = int(input("Fats: "))
        carbs = int(input("Carbs: "))
        food = Food(name, calories, protien, fats, carbs)
        today.append(food)
        print("Successfully added!")
    elif choice == "2":
        calorie_sum = sum(food.calories for food in today)
        protein_sum = sum(food.protein for food in today)
        fats_sum = sum(food.fat for food in today)
        carbs_sum = sum(food.carbs for food in today)
        fig, axs = plt.subplots(2,2)
        #"Macronutrients Distribution Pie chart
        axs[0, 0].pie([protein_sum, fats_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"], autopct = "%1.1f%%")
        axs[0, 0].legend()
        axs[0, 0].set_title("Macronutrients Distribution")
        #Top right chart Macronutrients Progress
        axs[0, 1].bar([0, 1, 2], [protein_sum, fats_sum, carbs_sum], width=0.4)
        axs[0, 1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, FAT_GOAL, CARB_GOAL], width=0.4)
        axs[0, 1].legend()
        axs[0, 1].set_title("Macronutrients Progress")
        #Calories Goal Progress Pie chart
        axs[1, 0].pie([calorie_sum, CALORIE_GOAL_LIMIT - calorie_sum], labels=["Calories", "Remaining"], autopct="%1.1f%%")
        axs[1, 0].set_title("Calories Goal Progress")
        axs[1, 0].legend()
        #line graph Calorie Goal Over Time
        axs[1, 1].plot(list(range(len(today))), np.cumsum([food.calories for food in today]), label="Calories Eaten")
        axs[1, 1].plot(list(range(len(today))), [CALORIE_GOAL_LIMIT] * len(today), label="Calorie Goal")
        axs[1, 1].legend()
        axs[1, 1].set_title("Calorie Goal Over Time")

        fig.tight_layout()
        print(plt.get_backend())
        plt.show()
    elif choice == "q":
        done = True
    else:
        print("Invalid Choice!")
    
