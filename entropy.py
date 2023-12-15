import numpy as np
import math


def total(data):
    """Calcualte the entropy for each feature

    Args:
        feature (pandas dataframe):  It is a dataframe containing the feature
        and the label
    """

    class_counts = dict(zip(*np.unique(data[:, -1], return_counts=True)))
    entropy = 0

    if len(data) == 1:
        return 0

    for c in class_counts.keys():
        p = class_counts[c] / len(data)

        if p == len(np.unique(data[:, -1])) == 1:
            continue

        entropy += p * math.log(p, len(np.unique(data[:, -1])))

    return -entropy


def contiuous(data):
    """_summary_

    Args:
        data (_type_): _description_
    """

    data = data[data[:, 0].argsort()]

    split_points = np.zeros(len(data))
    sp_entropy = np.zeros(len(data))
    gain = np.zeros(len(data))

    for i in range(len(data) - 1):
        j = i + 1

        if data[i, 1] != data[j, 1]:
            split_points[i] = (data[i, 0] + data[j, 0]) / 2

    for idx, sp in enumerate(split_points):
        if sp > 0:
            sp_entropy[idx] = total(data[: idx + 1]) + total(data[idx + 1 :])

    for idx, sp in enumerate(sp_entropy):
        if sp > 0:
            gain[idx] = total(data) - sp

    split_index = np.argmax(gain)

    best_split_point = split_points[split_index]
    best_entropy = sp_entropy[split_index]
    best_gain = gain[split_index]

    return best_split_point, best_entropy, best_gain
