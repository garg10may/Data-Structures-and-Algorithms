# prefix sums
from itertools import combinations
from itertools import accumulate
from itertools import chain
from itertools import permutations


def prefix_sums(arr):
    combs = []
    for i in range(1, len(arr)+1):
        combs.extend(list(combinations(arr, i)))
    return combs

# print(prefix_sums([1, 2, 3, 4, 5]))


s = 'abc'

#using knapscak find permutations

def all_combinations(s):
    result = []
    def backtrack(start, path):
        if path:
            result.append(''.join(path))
        for i in range(start, len(s)):
            backtrack(i + 1, path + [s[i]])
    backtrack(0, [])
    return result

print(all_combinations('abc'))  # Output: ['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']

def combinations(s, k):
    result = []
    if k == 0:
        return ['']
    if not s or k < 0:
        return []
    # Include s[0]
    with_first = [s[0] + comb for comb in combinations(s[1:], k-1)]
    # Exclude s[0]
    without_first = combinations(s[1:], k)
    result.extend(with_first)
    result.extend(without_first)
    return result

print(combinations(s, 2))

    