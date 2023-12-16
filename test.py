import pandas as pd
from tree import DecisionTree


df = pd.read_csv("./data.csv", delimiter=";")


tree = DecisionTree([f for f in df.columns if f != "class"], df)


tree.build()
