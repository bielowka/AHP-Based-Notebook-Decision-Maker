from Matrix import Matrix


class Object_comparison_layer:
    def __init__(self, num_of_objects, criteria):
        self.Cs = []
        self.num_of_criteria = len(criteria)
        self.num_of_objects = num_of_objects
        self.criteria = criteria
        self.Ws = []

        for i in range(self.num_of_criteria):
            c = Matrix(num_of_objects)
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
        for i in range(self.num_of_criteria):
            pass
            # TODO
            # rządaj wyniku porównania każdej pary przedmiotów w danym kryterium
            # w losowej kolejności
