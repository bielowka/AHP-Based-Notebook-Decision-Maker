import itertools
import tkinter as tk


class results_presentation:
    def __init__(self, ranking, inconsistencies=None):
        self.ranking = ranking
        self.inconsistencies = inconsistencies

        window = tk.Tk()

        frame = tk.Frame(
            master=window,
            borderwidth=1,
            relief=tk.RAISED
        )

        for i in range(len(ranking)):
            label = tk.Label(master=frame, text="Place {place}:  Laptop {id}".format(place=i + 1, id=ranking[i][1]),
                             font=("Verdana", 20 - i, "bold"))
            label.pack()

        flatten_list = list(itertools.chain.from_iterable(self.inconsistencies))
        data = ["{title} : {val}".format(title=x[1], val=x[0]) for x in flatten_list]
        selected = tk.StringVar()
        selected.set(data[0])
        self.dropdown = tk.OptionMenu(frame, selected, *data)

        btn = tk.Button(frame, text="Show inconsistency indexes", command=self.show_inconsistency)
        btn.pack()

        for i in range(len(ranking)):
            label = tk.Label(master=frame,
                             text="Laptop {id} ranking value {val}".format(id=ranking[i][1], val=ranking[i][0]),
                             font=("Verdana", 10))
            label.pack()

        frame.pack()

        window.mainloop()

    def show_inconsistency(self):
        self.dropdown.pack()
