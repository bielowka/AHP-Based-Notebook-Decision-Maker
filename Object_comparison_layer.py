import itertools
import random

import scipy.special
from Matrix import Matrix


class Object_comparison_layer:
    def __init__(self, num_of_objects, criteria):
        self.Cs = []
        self.num_of_criteria = len(criteria)
        self.num_of_objects = num_of_objects
        self.criteria = criteria
        self.Ws = []
        self.num_of_pages = self.num_of_criteria * int(scipy.special.binom(self.num_of_objects, 2))

        for i in range(self.num_of_criteria):
            c = Matrix(num_of_objects, self.criteria, "objectCrit" + str(i))
            self.Cs.append(c)

    def check_fullness(self):
        for C in self.Cs:
            if not C.is_full():
                print(self.Cs.index(C), " criterium not ready")

    def prioritization(self):
        for C in self.Cs:
            if not C.is_full():
                C.completer()
            self.Ws.append(C.to_vector())
        return self.Ws

    def expertise(self):
        for o in range(self.num_of_criteria):
            pairs = [pair for pair in itertools.combinations([x for x in range(self.num_of_objects)],2)]
            used = [False for _ in range(len(pairs))]
            while False in used:
                i = random.randint(0,len(pairs)-1)
                if not used[i]:
                    used[i] = True
                    yield pairs[i],self.Cs[o]