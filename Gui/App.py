import tkinter as tk
from tkinter import font as tkfont, HORIZONTAL, LEFT, TOP
from DataPresentation import data_presentation


class App(tk.Tk):
    def __init__(self, layer, data, objects_num, exp_id=0, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        if not hasattr(layer, "num_of_pages") or not hasattr(layer, "expertise"):
            print("Object passed does not implement required methods")
            return

        self.layer = layer
        self.comparisons = layer.expertise()
        self.num_of_pages = layer.num_of_pages

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.wm_title("You are Expert number {id}".format(id=exp_id))

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}

        self.register_frame(container, 0, "first", None, self.layer)
        for i in range(1, self.num_of_pages + 1):
            self.register_frame(container, i, "question", self.comparisons, self.layer)
        self.register_frame(container, self.num_of_pages + 1, "last", None, self.layer)

        self.show_frame(0)
        _ = data_presentation(data, objects_num)

    def register_frame(self, container, page_id: int, page_type: str, generator, layer):
        if page_type == "first": frame = StartPage(parent=container, controller=self, page_id=page_id, layer=layer)
        if page_type == "question": frame = QuestionPage(parent=container, controller=self, page_id=page_id,
                                                         generator=generator, layer=layer)
        if page_type == "last": frame = LastPage(parent=container, controller=self, page_id=page_id, layer=layer)
        self.frames[page_id] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_id):
        frame = self.frames[page_id]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller, page_id, layer):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page_id = page_id
        label = tk.Label(self, text="Comparing " + layer.title, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame(1))
        button1.pack(side="bottom", fill="x")


class QuestionPage(tk.Frame):
    def __init__(self, parent, controller, page_id, generator, layer):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page_id = page_id
        self.layer = layer
        (self.inx1, self.inx2), self.matrix = next(generator)
        if self.matrix.title == "criteria":
            label = tk.Label(self, text="Is " + str(self.inx1) + " more important than " + str(self.inx2),
                             font=controller.title_font)
        else:
            label = tk.Label(self, text="Is " + str(self.inx1) + " better than " + str(self.inx2) + self.matrix.title,
                             font=controller.title_font)

        label.pack(side="top", fill="x", pady=10)

        self.choice = tk.Scale(self, from_=0, to=16, length=300, showvalue=0, orient=HORIZONTAL)
        self.choice.set(8)
        self.choice.pack()
        labels = tk.Frame(self, width=300)
        if self.matrix.title == "criteria":
            choicelabel = tk.Label(labels, text="Less important")
            choicelabel.pack(expand=True, side=LEFT, fill="x")
            choicelabel = tk.Label(labels, text="Similar")
            choicelabel.pack(expand=True, side=LEFT, fill="x")
            choicelabel = tk.Label(labels, text="More important")
            choicelabel.pack(expand=True, side=LEFT, fill="x")
            labels.pack(expand=True, side=TOP, fill="x")
        else:
            choicelabel = tk.Label(labels, text="Worse")
            choicelabel.pack(expand=True, side=LEFT, fill="x")
            choicelabel = tk.Label(labels, text="Similar")
            choicelabel.pack(expand=True, side=LEFT, fill="x")
            choicelabel = tk.Label(labels, text="Better")
            choicelabel.pack(expand=True, side=LEFT, fill="x")
            labels.pack(expand=True, side=TOP, fill="x")

        button = tk.Button(self, text="Go to the next page",
                           command=self.show_values)
        button.pack(side="bottom", fill="x")

    def show_values(self):
        map_ = [1 / 9, 1 / 8, 1 / 7, 1 / 6, 1 / 5, 1 / 4, 1 / 3, 1 / 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if self.matrix.title == "criteria":
            self.matrix.put_crit(self.inx1, self.inx2, map_[self.choice.get()])
        else:
            self.matrix.put_obj(self.inx1, self.inx2, map_[self.choice.get()])

        self.controller.show_frame(self.page_id + 1)


class LastPage(tk.Frame):
    def __init__(self, parent, controller, page_id, layer):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page_id = page_id
        self.layer = layer
        button = tk.Button(self, text="Go to the next comparison",
                           command=self.button_action)
        button.pack(side="bottom", fill="x")

    def button_action(self):
        self.controller.destroy()
