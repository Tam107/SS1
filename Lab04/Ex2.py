def sortList(lst):
    """
    Sorts a list of string in ascending order based on the length of each item.
    """
    lst.sort(key=lambda x: len(x))
    return lst

print(sortList(['Computer','Hello','Program','Languages','Python']))

def sortList_bubble(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(lst[j]) > len(lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


import numpy as np

def sortList_numpy(lst):
    lengths = np.array([len(s) for s in lst])
    sorted_indices = np.argsort(lengths)
    return [lst[i] for i in sorted_indices]