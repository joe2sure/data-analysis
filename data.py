import pandas as pd
import numpy as np

# create simple dataset
data = {
    "Name": ["Chuks", "Joe", "Charlie", "Bob"],
    "Age": [20, 21, 22],
    "Salary": [5000, 6000, 7000]
}

# convert to Dataframe
df = pd.DataFrame(data)

# perform some analyze
print("Dataset:")
print(df)