from node import Node
from utils import find_split_criterion
import numpy as np


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
        self.node_stack = [self.root]

    def split(self):
        if not self.split_possible():
            return False

        feature_name, best_split_point = find_split_criterion(
            self.current_node.samples, self.features_list
        ).values()

        if best_split_point == -1:
            return False

        # print("feature_name: ", feature_name)
        # print("best_split_point: ", best_split_point)

        self.current_node.feature_name = feature_name
        self.current_node.split_value = best_split_point

        sorted_df = self.current_node.samples.sort_values(
            by=self.current_node.feature_name
        )

        # Split the DataFrame into two based on the provided value
        left_split = sorted_df[sorted_df[feature_name] <= self.current_node.split_value]
        right_split = sorted_df[sorted_df[feature_name] > self.current_node.split_value]

        self.current_node.is_leaf = False
        self.current_node.samples = None

        self.current_node.left = Node(
            is_leaf=True,
            split_value=None,
            left=None,
            right=None,
            class_label=None,
            feature_name=None,
            samples=left_split,
        )
        self.current_node.left.assign_class()

        self.current_node.right = Node(
            is_leaf=True,
            split_value=None,
            left=None,
            right=None,
            class_label=None,
            feature_name=None,
            samples=right_split,
        )

        self.current_node.right.assign_class()

        return True

    def build(self):
        while len(self.node_stack) > 0:
            # print("\n\n\n========================\n\n\n")
            # print("STACK OG", self.node_stack, "\n\n")

            new_nodes = self.node_stack[:]

            for node in self.node_stack:
                print("\n\n+++++++++++++++++++\n\n")
                self.current_node = node
                print("current_node: ", self.current_node)

                if self.split():
                    print("LEFT: ", self.current_node.left)
                    print("RIGHT: ", self.current_node.right, "\n\n")

                    new_nodes.extend([self.current_node.left, self.current_node.right])
                new_nodes.pop(0)
                self.current_node.print_attr()

                # print("\n\nSTACK EDITED", new_nodes, "\n\n")

            self.node_stack = new_nodes

    def split_possible(self):
        if len(np.unique(self.current_node.samples["class"].values)) == 1:
            return False
        return True
