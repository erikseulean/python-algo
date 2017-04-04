from copy import deepcopy


def get_subsets(set):

    if len(set) == 0:
        return None

    subset = [[]]
    for item in set:
        newset = []
        for ss in subset:
            copied_set = deepcopy(ss)
            copied_set.append(item)
            newset.append(copied_set)
        subset.extend(newset)
    return subset


print(get_subsets([1, 2, 3, 4]))
