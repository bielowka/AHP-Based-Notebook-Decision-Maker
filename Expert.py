class Expert:
    def __init__(self, id, priority, criteria, has_subcriteria, crit_to_subcrit):
        self.id = id
        self.priotiy = priority
        self.criteria = criteria
        self.has_subcriteria = has_subcriteria
        self.crit_to_subcrit = crit_to_subcrit
        self.subcrit_matrices = [[] if self.has_subcriteria[i] else None for i in range(len(criteria))]  # list of lists of obj comparison matrices
        self.subcrit_importance_matrices = [[] if self.has_subcriteria[i] else None for i in range(len(criteria))]  # list of importance matrices
        self.crit_matrices = [None if self.has_subcriteria[i] else [] for i in range(len(criteria))]  # list of object comparison matrices for flat criteria
        self.importance_matrix = []

    def show(self):
        for i in range(len(self.criteria)):
            print(self.criteria[i],": ")
            if self.has_subcriteria[i]:
                print("Crit matrixes:")
                print(self.subcrit_matrices[i])
                print("Importance matrix:")
                print(self.subcrit_importance_matrices[i])
            else:
                print("Crit matrix:")
                print(self.crit_matrices[i])

        print("C:")
        print(self.importance_matrix)