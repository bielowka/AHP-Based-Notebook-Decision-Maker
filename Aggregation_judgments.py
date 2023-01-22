from Matrix import Matrix

class AggregationJudgments:
    def __init__(self, num_of_experts, num_of_objects, experts_importance, list_of_matrix):
        self.num_of_experts = num_of_experts
        self.num_of_objects = num_of_objects
        self.experts_importance = experts_importance
        self.list_of_matrix = list_of_matrix
        self.matrix = Matrix(self.num_of_objects, [], "object_judgment_by_criteria")

    def calculate_geometric_mean(self, x, y):
        result = 1
        for i in range(self.num_of_experts):
            result *= self.list_of_matrix[i][x][y] ** self.experts_importance[i]
        return result ** (1/self.num_of_experts)

    def get_aggregated_matrix(self):
        for i in range(self.num_of_objects):
            for j in range(i,self.num_of_objects):
                self.matrix.put_obj(i,j,self.calculate_geometric_mean(i,j))

if __name__ == "__main__":
    k = AggregationJudgments(4,3,[1,1,1,1],[[[1,2,4/5],[1/2,1,1/4],[5/4,4,1]],
                                        [[1,2,1/4],[1/2,1,8/9],[4,9/8,1]],
                                        [[1,1,3/8],[1,1,2/5],[8/3,5/2,1]],
                                        [[1,1,3/7],[1,1,8/9],[7/3,9/8,1]]])
    print(k.get_aggregated_matrix())
    print(k.matrix.to_vector())
    # print(k.calculate_geometric_mean(0,1))


