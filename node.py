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
