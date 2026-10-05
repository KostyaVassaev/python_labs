import sys
import os

sys.path.append(os.path.abspath("../lib"))

from arrays import *

#print([3, -1, 5, 5, 0], "->", min_max([3, -1, 5, 5, 0]))
#print([42], "->", min_max([42]))
#print([-5, -2, -9], "->", min_max([-5, -2, -9]))
#print([], "->", min_max([]))
#print([1.5, 2, 2.0, -3.1], "->", min_max([1.5, 2, 2.0, -3.1]))

#print([3, 1, 2, 1, 3], "->", unique_sorted([3, 1, 2, 1, 3]))
#print([], "->", unique_sorted([]))
#print([-1, -1, 0, 2, 2], "->", unique_sorted([-1, -1, 0, 2, 2]))
#print([1.0, 1, 2.5, 2.5, 0], "->", unique_sorted([1.0, 1, 2.5, 2.5, 0]))

#print([[1, 2], [3, 4]], "->", flatten([[1, 2], [3, 4]]))
#print([[1, 2], (3, 4, 5)], "->", flatten([[1, 2], (3, 4, 5)]))
#print([[1], [], [2, 3]], "->", flatten([[1], [], [2, 3]]))
#print([[1, 2], "ab"], "->", flatten([[1, 2], "ab"]))