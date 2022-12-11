import unittest
from Vectors_calculations import Vectors_calculations

class Vectors_calculations_test(unittest.TestCase):

    def test_calculatinf_subcriteria(self):
        num_of_objects = 4
        num_of_criteria = 3
        objects_comparison_vectors = [[0.208, 0.226, 0.343, 0.22], [0.398, 0.24, 0.213, 0.146],
                                      [0.250, 0.279, 0.216, 0.253]]
        criteria_comparison_vector = [0.776, 0.153, 0.07]
        vectors_calculations = Vectors_calculations(num_of_objects, num_of_criteria, objects_comparison_vectors,
                                                    criteria_comparison_vector)
        result = round(vectors_calculations.calculate_object_value(0),2)
        self.assertEqual(result, 0.24)

if __name__ == '__main__':
    unittest.main()