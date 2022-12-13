# import numpy as np
# from numpy.linalg import eig
#
#
# def normalize(x):
#     fac = abs(x).max()
#     x_n = x / x.max()
#     return fac, x_n
#
#
# def to_vector(A):
#     w, v = eig(A)
#
#     vec = [x[0].real for x in v]
#     norm = [x / sum(vec) for x in vec]
#     return norm

from Gui.App import App
from Object_comparison_layer import Object_comparison_layer
from Criteria_weight_layer import Criteria_comparison_layer
from Vectors_calculations import Vectors_calculations

if __name__ == "__main__":
    # criteria = ["A","B","C","D","E","F"]
    # objects_num = 3
    # object_comparison_layer = Object_comparison_layer(objects_num,criteria)
    # criteria_comparison_layer = Criteria_comparison_layer(criteria)
    #
    # app = App(object_comparison_layer)
    # app.mainloop()
    #
    # for x in object_comparison_layer.Cs: print(x)  # macierze wypełnione porównań
    #
    # app = App(criteria_comparison_layer)
    # app.mainloop()
    #
    # print(criteria_comparison_layer.C)  #macierz wypelniona wag kryteriów
    #
    # # TODO: tutaj obie warstwy powinny juz byc uzupelnione

    criteria = ["Rozmiar","Cena",'Wygląd',"Bateria","Specyfikacja","System operacyjny",]
    has_subcriteria = [True,False,True,True,True,False]
    subcriteria0 = ["waga","przekotna"]
    subcriteria2 = ["wewn","zewn"]
    subcriteria3 = ["pojemnosc","czas ładowania"]
    subcriteria4 = [
        "procesor",
        "karta graficzna",
        "pamięć RAM",
        "dysk",
        "rodzielczość ekranu",
    ]
    crit_to_subcrit = [subcriteria0,None,subcriteria2,subcriteria3,subcriteria4,None]
    subcrit_ready_matrixes = []

    objects_num = 2

    for i in range(len(criteria)):
        if has_subcriteria[i]: #  jeśli ma podkryteria no to uruchamiamy na nich obie wartstwy
            object_comparison_layer = Object_comparison_layer(objects_num,crit_to_subcrit[i])
            criteria_comparison_layer = Criteria_comparison_layer(crit_to_subcrit[i])

            app = App(object_comparison_layer)
            app.mainloop()

            vectors = [x.to_vector() for x in object_comparison_layer.Cs]

            app = App(criteria_comparison_layer)
            app.mainloop()

            C = criteria_comparison_layer.C

            vectors_calculations = Vectors_calculations(objects_num,len(C.to_vector()), vectors, C.to_vector())
            objects_values = vectors_calculations.objects_values()
            subcrit_ready_matrixes.append(objects_values)
            # TODO: use Vectors_calculations on 'vectors' and 'C', then append result to subcrit_ready_matrixes
            # (chcemy mieć gotowe wektory rankingów do wykorzystania później razem z wektorami z zwykłych kryteriów)

    flat_criteria = [criteria[i] for i in range(len(criteria)) if not has_subcriteria[i]] # flat no to te bez pod kryteriów

    object_comparison_layer = Object_comparison_layer(objects_num,flat_criteria)
    app = App(object_comparison_layer)
    app.mainloop()

    flat_criteria_vectors = [x.to_vector() for x in object_comparison_layer.Cs] # licze je normalnie

    vectors = [] # tu będą wektory raningowe wszystkich kryteriów

    for i in range(len(criteria)): # tutaj brzydkie appendowanie po kolei, żeby mieć listę wektorów już wszystkich kryteriów po kolei,
                                        # i tych z i tych bez podkryteriów
        if has_subcriteria[i]:
            vectors.append(subcrit_ready_matrixes[0])
            subcrit_ready_matrixes.remove(0)
        else:
            vectors.append(flat_criteria_vectors[0])
            flat_criteria_vectors.remove(0)

    criteria_comparison_layer = Criteria_comparison_layer(criteria)
    app = App(criteria_comparison_layer)
    app.mainloop()

    C = criteria_comparison_layer.C # tu masz macierz wag wszystkich kryteriów
    print(Vectors_calculations(len(vectors),len(C.to_vector()), vectors, C.to_vector()))
    # TODO: use Vector_calculations on 'vectors' and 'C' to achieve final ranking
    # TODO: print final ranking