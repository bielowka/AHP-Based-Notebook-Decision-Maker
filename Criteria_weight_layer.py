import itertools
import random

import scipy.special

from Matrix import Matrix

class Criteria_comparison_layer():
    def __init__(self, criteria, title=""):
        self.title = title
        self.criteria = criteria
        self.num_of_criteria = len(criteria)
        self.C = Matrix(self.num_of_criteria,criteria,"criteria")
        self.num_of_pages = int(scipy.special.binom(self.num_of_criteria, 2))

    def check_fullness(self):
        if not self.C.is_full():
            print("C is not full")

    def prioritization(self):
        if not self.C.is_full():
            self.C.completer()
        return self.C.to_vector()

    def expertise(self):
        pairs = [pair for pair in itertools.combinations(self.criteria, 2)]
        used = [False for _ in range(len(pairs))]
        while False in used:
            i = random.randint(0, len(pairs)-1)
            if not used[i]:
                used[i] = True
                yield pairs[i],self.C
            # TODO


