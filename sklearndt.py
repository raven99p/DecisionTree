from sklearn import tree
import pandas as pd
import matplotlib.pyplot as plt


clf = tree.DecisionTreeClassifier(random_state=0, max_depth=3, criterion="entropy")
df = pd.read_csv("./data.csv", delimiter=";")

clf = clf.fit(df[[c for c in df.columns if c != "class"]].values, df["class"].values)
tree.plot_tree(clf)

plt.show()
