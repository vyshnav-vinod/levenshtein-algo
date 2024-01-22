# https://en.wikipedia.org/wiki/Levenshtein_distance

import sys

def algo(word1, word2):
    if len(word1) == 0:
        return len(word2)
    elif len(word2) == 0:
        return len(word1)
    elif word1[0] == word2[0]:
        return algo(word1[1:], word2[1:])
    else:
        return 1 + min(algo(word1[1:], word2), algo(word1, word2[1:]), algo(word1[1:], word2[1:]))


edit_dist = algo(sys.argv[1], sys.argv[2])
print(edit_dist)
