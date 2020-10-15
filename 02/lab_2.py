# Import the necessary libraries (numpy and pandas)
import numpy as np
import pandas as pd

# Import the Pokemon dataset available at https://www.kaggle.com/alopez247/pokemon
pokemon = pd.read_csv("pokemon.csv")

# Sort by attack power from high to low
print(pokemon.Attack.sort_values)

# Describe the defense power for each Pokemon type
print("-------------------")
print(pokemon.groupby("Type_1").Defense.describe())

# What are the mean, median, max and minimum of the total column for each Pokemon type?
print("-------------------")
print(pokemon.groupby('Type_1').Total.agg(["mean", "min", "max", "median"]))

# What is the most common Pokemon type?
print("-------------------")
print("The most common Pokemon type is", pokemon["Type_1"].value_counts().idxmax())


# NOTE:
# Series.value_counts()
# Return a Series containing counts of unique values.

# Series.idxmax()
# Return the row label of the maximum value.