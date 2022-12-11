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

if __name__ == "__main__":
    criteria = ["A","B","C","D","E","F"]
    objects_num = 3
    object_comparison_layer = Object_comparison_layer(objects_num,criteria)
    criteria_comparison_layer = Criteria_comparison_layer(criteria)

    app = App(object_comparison_layer)
    app.mainloop()

    for x in object_comparison_layer.Cs: print(x)  # macierze wypełnione porównań

    app = App(criteria_comparison_layer)
    app.mainloop()

    print(criteria_comparison_layer.C)  #macierz wypelniona wag kryteriów

    # TODO: tutaj obie warstwy powinny juz byc uzupelnione
