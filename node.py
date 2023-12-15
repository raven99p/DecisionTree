class Node:
    def __init__(
        self, id, is_leaf, split_value, left, right, class_label, feature_index
    ):
        self.id = id
        self.is_leaf = is_leaf
        self.split_value = split_value
        self.left = left
        self.right = right
        self.class_label = class_label
        self.feature_index = feature_index

    def print_attr(self):
        print(vars(self))
