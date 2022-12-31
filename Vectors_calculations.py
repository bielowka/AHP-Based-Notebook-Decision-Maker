import numpy as np


class Vectors_calculations:
    def __init__(self, num_of_objects, num_of_criteria, objects_comparison_vectors, criteria_comparison_vector):
        self.num_of_objects = num_of_objects
        self.num_of_criteria = num_of_criteria
        self.objects_comparison_vectors = objects_comparison_vectors
        self.criteria_comparison_vector = criteria_comparison_vector

    def calculate_object_value(self, index):
        sum_elements = []
        for i in range(self.num_of_criteria):
            sum_elements.append(self.criteria_comparison_vector[i] * self.objects_comparison_vectors[i][index])
        return np.round(sum(sum_elements), 3)

    def objects_values(self):
        values = []
        for i in range(self.num_of_objects):
            values.append(self.calculate_object_value(i))
        return values
