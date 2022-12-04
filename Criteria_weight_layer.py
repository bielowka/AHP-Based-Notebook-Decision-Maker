from Matrix import Matrix


class Criteria_comparison_layer:
    def __init__(self, criteria):
        self.criteria = criteria
        self.num_of_criteria = len(criteria)
        self.C = Matrix(self.num_of_criteria)

    def check_fullness(self):
        if not self.C.is_full():
            print("C is not full")

    def prioritization(self):
        if not self.C.is_full():
            self.C.completer()
        return self.C.to_vector()

    def expertise(self):
        for i, j in range(self.num_of_criteria):
            pass  # TODO
            # rządaj wyniku porównania każdej kryteriów
            # w losowej kolejności
