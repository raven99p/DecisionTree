import numpy as np


class Node:
    def __init__(
        self,
        is_leaf,
        split_value,
        left,
        right,
        class_label,
        feature_name,
        samples,
    ):
        self.is_leaf = is_leaf
        self.split_value = split_value
        self.left = left
        self.right = right
        self.class_label = class_label
        self.feature_name = feature_name
        self.samples = samples
        self.parent = None

    def print_attr(self):
        print(vars(self))

    def assign_class(self):
        # print("ASSING CLASS")
        if self.is_leaf:
            all_labels = self.samples["class"].values

            if len(np.unique(all_labels)) == 1:
                self.class_label = all_labels[0]
                # print("ASSIGNED CLASS TRUE")
