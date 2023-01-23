from Gui.App import App
from Object_comparison_layer import Object_comparison_layer
from Criteria_weight_layer import Criteria_comparison_layer
from Vectors_calculations import Vectors_calculations
from Consistency_index import Saaty_index
from ResultsPresentation import results_presentation
from Expert import Expert
from Aggregation_judgments import AggregationJudgments
from Aggregation_priorities import AggregationPriorities


def experts_answer(expert):
    for i in range(len(criteria)):
        if has_subcriteria[i]:
            object_comparison_layer = Object_comparison_layer(objects_num, crit_to_subcrit[i],
                                                              "objects in subcriteria of " + criteria[i])
            criteria_comparison_layer = Criteria_comparison_layer(crit_to_subcrit[i],
                                                                  "importance of subcriteria of " + criteria[i])
            app = App(object_comparison_layer, objects_data, objects_num, expert.id)
            app.mainloop()

            expert.subcrit_matrices[i] = [x.A for x in object_comparison_layer.Cs]

            app = App(criteria_comparison_layer, objects_data, objects_num, expert.id)
            app.mainloop()

            C = criteria_comparison_layer.C
            expert.subcrit_importance_matrices[i] = C

    flat_criteria = [criteria[i] for i in range(len(criteria)) if not has_subcriteria[i]]
    flat_criteria_idx = [i for i in range(len(criteria)) if not has_subcriteria[i]]

    object_comparison_layer = Object_comparison_layer(objects_num, flat_criteria, "objects in criteria")
    app = App(object_comparison_layer, objects_data, objects_num, expert.id)
    app.mainloop()

    matrices = [x.A for x in object_comparison_layer.Cs]
    for i in range(len(flat_criteria_idx)):
        expert.crit_matrices[flat_criteria_idx[i]] = matrices[i]

    criteria_comparison_layer = Criteria_comparison_layer(criteria, "importance of each criteria")
    app = App(criteria_comparison_layer, objects_data, objects_num, expert.id)
    app.mainloop()

    C = criteria_comparison_layer.C
    expert.importance_matrix = C


if __name__ == "__main__":
    # DATA
    criteria = ["Cena", 'Wygląd', "Bateria", "Specyfikacja"]
    has_subcriteria = [False, False, True, True]
    subcriteria2 = ["Pojemnosc baterii", "Czas ładowania"]
    subcriteria3 = [
        "Procesor",
        "Karta graficzna",
        "Pamięć RAM",
        "Dysk",
        "Rodzielczość ekranu",
    ]
    crit_to_subcrit = [None, None, subcriteria2, subcriteria3]

    objects_num = 3
    objects_data = [
        [0, "Lenovo Yoga Slim 7 Pro 14ITL5", "1,3 kg", "14\"", "4400 zł", "lap1z.jpg", "lap1w.jpg", "61 Wh",
         "1h 40 min", "Intel® Core™ i5 11gen", "Intel® Iris Xe Graphics", "16 GB", "512 GB", "2240 x 1400 pikseli",
         "Windows 10 Home Edition"],
        [1, "DELL Inspiron 5415-8741", "1,44 kg", "14 \"", "4800 zł", "lap2z.jpeg", "lap2w.jpg", "54 Wh", "1h 20 min",
         "AMD Ryzen™ 7 5700U", "AMD Radeon™ Graphics", "16 GB", "512 GB", "1920 x 1080 pikseli",
         "Windows 11 Professional"],
        [2, "HP Envy 13", "1,23 kg", "13,3\"", "4 700 zł", "lap3z.jpg", "lap3w.jpg", "58 Wh", "1h 30 min",
         "Intel Core i5-1135G7", "Intel Iris Xe Graphics", "16 GB", "512 GB", "1920 x 1080 pikseli", "Windows 11 Home"]
    ]

    # PROPERTIES
    SHOW_INCONSISTENCY = True
    NUMBER_OF_EXPERTS = 2
    EXPERTS_PRIORITIES = [0.7, 0.3]
    assert sum(EXPERTS_PRIORITIES) == 1

    # MAIN
    experts = [Expert(i, EXPERTS_PRIORITIES[i], criteria, has_subcriteria, crit_to_subcrit) for i in range(NUMBER_OF_EXPERTS)]

    for e in experts:
        experts_answer(e)

    if SHOW_INCONSISTENCY:
        subcrit_matrixes_for_idx = []

    subcrit_vectors = []

    for i in range(len(criteria)):
        if has_subcriteria[i]:
            matrices = []
            tmp = [e.subcrit_matrices[i] for e in experts]
            for j in range(len(crit_to_subcrit[i])):
                tmp2 = []
                for x in range(NUMBER_OF_EXPERTS):
                    tmp2.append(tmp[x][j])
                agrr = AggregationJudgments(NUMBER_OF_EXPERTS,objects_num,EXPERTS_PRIORITIES,tmp2)
                matrices.append(agrr.get_aggregated_matrix())

            if SHOW_INCONSISTENCY:
                matricess = [(Saaty_index(x.A), x.title[12:]) for x in matrices]
                subcrit_matrixes_for_idx.append(matricess)

            vectors = [x.to_vector() for x in matrices]

            Cs = []
            for e in range(NUMBER_OF_EXPERTS):
                Cs.append(experts[e].subcrit_importance_matrices[i].to_vector())
            aggr = AggregationPriorities(NUMBER_OF_EXPERTS,len(crit_to_subcrit[i]),EXPERTS_PRIORITIES,Cs)
            C = aggr.get_aggregated_vector()

            vectors_calculations = Vectors_calculations(objects_num, len(C), vectors, C)
            objects_values = vectors_calculations.objects_values()
            subcrit_vectors.append(objects_values)

    flat_criteria = [criteria[i] for i in range(len(criteria)) if not has_subcriteria[i]]
    flat_criteria_idx = [i for i in range(len(criteria)) if not has_subcriteria[i]]
    flat_criteria_matrices = []

    for i in flat_criteria_idx:
        tmp = []
        for e in range(NUMBER_OF_EXPERTS):
            tmp.append(experts[e].crit_matrices[i])
        aggr = AggregationJudgments(NUMBER_OF_EXPERTS,len(flat_criteria),EXPERTS_PRIORITIES,tmp)
        flat_criteria_matrices.append(aggr.get_aggregated_matrix())

    flat_criteria_vectors = [x.to_vector() for x in flat_criteria_matrices]

    if SHOW_INCONSISTENCY:
        flat_criteria_matrices_for_idx = [[(Saaty_index(x.A), x.title[12:])] for x in flat_criteria_matrices]

    vectors = []
    for i in range(len(criteria)):
        if has_subcriteria[i]:
            vectors.append(subcrit_vectors[0])
            subcrit_vectors.pop(0)
        else:
            vectors.append(flat_criteria_vectors[0])
            flat_criteria_vectors.pop(0)

    Cs = []
    for e in range(NUMBER_OF_EXPERTS):
        Cs.append(experts[e].importance_matrix)
    aggr = AggregationPriorities(NUMBER_OF_EXPERTS, len(criteria), EXPERTS_PRIORITIES, [c.to_vector() for c in Cs])
    C = aggr.get_aggregated_vector()

    final_calculation = Vectors_calculations(objects_num, len(criteria), vectors, C)
    res_vec = final_calculation.objects_values()
    results = [(res_vec[i], i) for i in range(objects_num)]
    results.sort(key=lambda x: x[0]*(-1))

    results_presentation(results, subcrit_matrixes_for_idx + flat_criteria_matrices_for_idx if SHOW_INCONSISTENCY else None)



