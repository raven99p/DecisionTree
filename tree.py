from node import Node


class DecisionTree:
    def __init__(self):
        self.root = Node(
            id=0,
            is_leaf=False,
            split_value=None,
            left=None,
            right=None,
            class_label=None,
            feature_index=None,
        )

    def print_attr(self):
        print("Calling print attr of node...")
        self.root.print_attr()

    def add_node(self, id, children, is_leaf):
        pass
