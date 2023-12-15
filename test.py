import pandas as pd
from tree import DecisionTree

# import numpy as np
# import entropy

df = pd.read_csv("./data.csv", delimiter=";")

# features = [
#     "io",
#     "pa500",
#     "hfs",
#     "da",
#     "area",
#     "ada",
#     "maxip",
#     "dr",
#     "p",
# ]

# for f in features:
#     print(entropy.contiuous(df[[f, "class"]].values))


tree = DecisionTree()


tree.print_attr()
