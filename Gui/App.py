import tkinter as tk
from tkinter import font as tkfont, HORIZONTAL


class App(tk.Tk):
    def __init__(self,layer, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        if not hasattr(layer,"num_of_pages") or not hasattr(layer,"expertise"):
            print("Object passed does not implement required methods")
            return

        self.layer = layer
        self.comparisons = layer.expertise()
        self.num_of_pages = layer.num_of_pages

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.register_frame(container,0,"first",None,self.layer)
        for i in range(1,self.num_of_pages+1):
            self.register_frame(container,i,"question",self.comparisons,self.layer)
        self.register_frame(container,self.num_of_pages+1,"last",None,self.layer)

        self.show_frame(0)

    def register_frame(self, container, page_id: int, page_type: str, generator, layer):
        if page_type == "first": frame = StartPage(parent=container, controller=self, page_id=page_id,layer=layer)
        if page_type == "question": frame = QuestionPage(parent=container, controller=self, page_id=page_id,generator=generator, layer=layer)
        if page_type == "last": frame = LastPage(parent=container, controller=self, page_id=page_id,layer=layer)
        self.frames[page_id] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_id):
        frame = self.frames[page_id]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller,page_id,layer):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page_id = page_id
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame(1))
        button1.pack()


class QuestionPage(tk.Frame):
    def __init__(self, parent, controller,page_id,generator,layer):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page_id = page_id
        self.layer = layer
        (self.inx1, self.inx2), self.matrix = next(generator)
        label = tk.Label(self, text=str(self.inx1) + str(self.inx2) + "" + self.matrix.title, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.slider = tk.Scale(self, from_= 1, to=10, orient=HORIZONTAL)
        self.slider.pack()

        button = tk.Button(self, text="Go to the next page",
                           command=self.show_values)
        button.pack()

    def show_values(self):
        if self.matrix.title == "criteria":
            self.matrix.put_crit(self.inx1, self.inx2, self.slider.get())
        else:
            self.matrix.put_obj(self.inx1, self.inx2, self.slider.get())

        self.controller.show_frame(self.page_id + 1)


class LastPage(tk.Frame):
    def __init__(self, parent, controller, page_id,layer):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page_id = page_id
        self.layer = layer
        label = tk.Label(self, text="This is the last page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=self.button_action)
        button.pack()

    def button_action(self): pass
        # self.controller.show_frame(0)
