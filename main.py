from Gui.App import App
from Object_comparison_layer import Object_comparison_layer
from Criteria_weight_layer import Criteria_comparison_layer
from Vectors_calculations import Vectors_calculations
from Consistency_index import Saaty_index
from ResultsPresentation import results_presentation

if __name__ == "__main__":
    criteria = ["Rozmiar", "Cena", 'Wygląd', "Bateria", "Specyfikacja", "System operacyjny", ]
    has_subcriteria = [True, False, True, True, True, False]
    subcriteria0 = ["Waga", "Przekotna"]
    subcriteria2 = ["Wygląd wewnętrzny", "Wygląd zewnętrzny"]
    subcriteria3 = ["Pojemnosc baterii", "Czas ładowania"]
    subcriteria4 = [
        "Procesor",
        "Karta graficzna",
        "Pamięć RAM",
        "Dysk",
        "Rodzielczość ekranu",
    ]
    crit_to_subcrit = [subcriteria0, None, subcriteria2, subcriteria3, subcriteria4, None]

    objects_num = 4
    objects_data = [
        [0, "Lenovo Yoga Slim 7 Pro 14ITL5", "1,3 kg", "14\"", "4400 zł", "lap1z.jpg", "lap1w.jpg", "61 Wh",
         "1h 40 min", "Intel® Core™ i5 11gen", "Intel® Iris Xe Graphics", "16 GB", "512 GB", "2240 x 1400 pikseli",
         "Windows 10 Home Edition"],
        [1, "DELL Inspiron 5415-8741", "1,44 kg", "14 \"", "4800 zł", "lap2z.jpeg", "lap2w.jpg", "54 Wh", "1h 20 min",
         "AMD Ryzen™ 7 5700U", "AMD Radeon™ Graphics", "16 GB", "512 GB", "1920 x 1080 pikseli",
         "Windows 11 Professional"],
        [2, "HP Envy 13", "1,23 kg", "13,3\"", "4 700 zł", "lap3z.jpg", "lap3w.jpg", "58 Wh", "1h 30 min",
         "Intel Core i5-1135G7", "Intel Iris Xe Graphics", "16 GB", "512 GB", "1920 x 1080 pikseli", "Windows 11 Home"],
        [3, "Dell XPS 15 9520", "2 kg", "15,6\"", "12 000 zł", "lap4z.jpg", "lap4w.jpeg", "68 Wh", "1h 40 min",
         "Intel Core i7-12700H", "NVIDIA GeForce RTX 3050 Ti", "32 GB ", "512 GB", "1920 x 1200 pikseli",
         "Windows 11 Home"],
    ]

    SHOW_INCONSISTENCY = True

    subcrit_vectors = []
    if SHOW_INCONSISTENCY:
        subcrit_matrixes = []

    for i in range(len(criteria)):
        if has_subcriteria[i]:
            object_comparison_layer = Object_comparison_layer(objects_num, crit_to_subcrit[i],
                                                              "objects in subcriteria of " + criteria[i])
            criteria_comparison_layer = Criteria_comparison_layer(crit_to_subcrit[i],
                                                                  "importance of subcriteria of " + criteria[i])

            app = App(object_comparison_layer, objects_data, objects_num)
            app.mainloop()

            if SHOW_INCONSISTENCY:
                matrices = [(Saaty_index(x.A), x.title[12:]) for x in object_comparison_layer.Cs]
                subcrit_matrixes.append(matrices)

            vectors = [x.to_vector() for x in object_comparison_layer.Cs]

            app = App(criteria_comparison_layer, objects_data, objects_num)
            app.mainloop()

            C = criteria_comparison_layer.C
            vectors_calculations = Vectors_calculations(objects_num, len(C.to_vector()), vectors, C.to_vector())
            objects_values = vectors_calculations.objects_values()
            subcrit_vectors.append(objects_values)

    flat_criteria = [criteria[i] for i in range(len(criteria)) if not has_subcriteria[i]]

    object_comparison_layer = Object_comparison_layer(objects_num, flat_criteria, "objects in criteria")
    app = App(object_comparison_layer, objects_data, objects_num)
    app.mainloop()

    flat_criteria_vectors = [x.to_vector() for x in object_comparison_layer.Cs]
    if SHOW_INCONSISTENCY:
        flat_criteria_matrices = [[(Saaty_index(x.A), x.title[12:])] for x in object_comparison_layer.Cs]

    vectors = []

    for i in range(len(criteria)):
        if has_subcriteria[i]:
            vectors.append(subcrit_vectors[0])
            subcrit_vectors.pop(0)
        else:
            vectors.append(flat_criteria_vectors[0])
            flat_criteria_vectors.pop(0)

    criteria_comparison_layer = Criteria_comparison_layer(criteria, "importance of each criteria")
    app = App(criteria_comparison_layer, objects_data, objects_num)
    app.mainloop()

    C = criteria_comparison_layer.C
    final_calculation = Vectors_calculations(objects_num, len(criteria), vectors, C.to_vector())
    res_vec = final_calculation.objects_values()
    results = [(res_vec[i], i) for i in range(objects_num)]
    results.sort(key=lambda x: x[0])

    results_presentation(results, subcrit_matrixes + flat_criteria_matrices if SHOW_INCONSISTENCY else None)
