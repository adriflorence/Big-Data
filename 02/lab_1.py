# Import the necessary libraries (numpy and pandas)
import numpy as np
import pandas as pd

# Import the Pokemon dataset available at https://www.kaggle.com/alopez247/pokemon
pokemon = pd.read_csv("pokemon.csv")

# Print the first 10 entries
print(pokemon.head(10))

# How many observations and columns are there?
print(pokemon.shape)

# Print the names of all of the columns
print(pokemon.columns)