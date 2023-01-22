from Matrix import Matrix


class AggregationPriorities:
    def __init__(self, num_of_experts, num_of_objects, experts_importance, list_of_vectors):
        self.num_of_experts = num_of_experts
        self.num_of_objects = num_of_objects
        self.experts_importance = experts_importance
        self.list_of_vectors = list_of_vectors

    def get_aggregated_vector(self):
        vec = []
        for i in range(self.num_of_objects):
            sum = 0
            for j in range(self.num_of_experts):
                sum += self.experts_importance[i] * self.list_of_vectors[j][i]
            vec.append(sum)
        return vec