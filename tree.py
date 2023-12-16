from node import Node
from utils import find_split_criterion


class DecisionTree:
    def __init__(self, features_list, data):
        self.root = Node(
            is_leaf=True,
            split_value=None,
            left=None,
            right=None,
            class_label=None,
            feature_name=None,
            samples=data,
        )
        self.features_list = features_list
        self.data = data
        self.current_node = self.root

    def split(self):
        feature_name, best_split_point = find_split_criterion(
            self.current_node.samples
        ).values()

        print(feature_name, best_split_point)

        self.current_node.feature_name = feature_name
        self.current_node.split_value = best_split_point

        sorted_df = self.current_node.samples.sort_values(
            by=self.current_node.feature_name
        )

        # Split the DataFrame into two based on the provided value
        left_split = sorted_df[sorted_df[feature_name] <= self.current_node.split_value]
        right_split = sorted_df[sorted_df[feature_name] > self.current_node.split_value]

        self.current_node.is_leaf = False

        self.current_node.left = Node(
            is_leaf=True,
            split_value=None,
            left=None,
            right=None,
            class_label=None,
            feature_name=None,
            samples=left_split,
        )

        self.current_node.right = Node(
            is_leaf=True,
            split_value=None,
            left=None,
            right=None,
            class_label=None,
            feature_name=None,
            samples=right_split,
        )

        print("current_node: ")
        self.current_node.print_attr()
