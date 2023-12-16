import entropy


def find_split_criterion(data, features_list):
    # print("data: ", data)
    # print("features_list: ", features_list)

    max_gain = 0
    feature = None

    for f in features_list:
        best_split_point, best_entropy, best_gain = entropy.contiuous(
            data[[f, "class"]].values
        )

        if best_gain > max_gain:
            max_gain = best_gain

        feature = {"name": f, "best_split_point": best_split_point}

    if max_gain == 0 or best_split_point == 0:
        return {"name": "end_of_tree", "best_split_point": -1}

    return feature
