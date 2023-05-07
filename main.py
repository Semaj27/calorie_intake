from dataclasses import dataclass

import numpy as np
import matplotlib as plt


CALORIE_GOAL_LIMIT = 3000   # kcal
PROTEIN_GOAL= 180   # grams
FAT_GOAL = 80   # grams
CARB_GOAL = 300   # grams

today = []


class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int
