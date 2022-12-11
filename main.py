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
    # app = App(Object_comparison_layer(2,["prize","speed"]))
    app = App(Criteria_comparison_layer(["A","B","C","D","E","F"]))
    app.mainloop()
