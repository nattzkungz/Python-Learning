a = {1:[55,20], 2:[20,50]}

import itertools

b = dict(list(itertools.combinations(a, 2)))

print(b)