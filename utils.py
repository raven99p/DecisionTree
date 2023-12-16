import entropy


def find_split_criterion(data):
    features = [
        "io",
        "pa500",
        "hfs",
        "da",
        "area",
        "ada",
        "maxip",
        "dr",
        "p",
    ]

    max_entropy = 0
    feature = None

    for f in features:
        best_split_point, best_entropy, best_gain = entropy.contiuous(
            data[[f, "class"]].values
        )
        if best_entropy > max_entropy:
            feature = {"name": f, "best_split_point": best_split_point}

    return feature
