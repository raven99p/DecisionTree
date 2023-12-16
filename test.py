import pandas as pd
from tree import DecisionTree
from utils import find_split_criterion
# import numpy as np
# import entropy

df = pd.read_csv("./data.csv", delimiter=";")

# print(find_split_criterion(df))


tree = DecisionTree(df.columns, df)


tree.split()
