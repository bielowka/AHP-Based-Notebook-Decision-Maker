import tkinter as tk

from PIL import ImageTk, Image


class data_presentation:
    def __init__(self, data, objects_num):
        window = tk.Toplevel()
        window.title("Data")

        n = objects_num

        label_frame = tk.Frame(window, width=100, height=400)
        label_frame.grid(row=1, column=0)

        labels = [tk.Label(label_frame, text="{data}".format(data=j)) for j in
                  ["numer w rankingu", "nazwa", "waga", "przekątna ekranu", "cena", "zewnętrzny", "wewnętrzny",
                   "pojemnosc", "czas ładowania", "procesor", "karta graficzna", "pamięć RAM", "dysk",
                   "rodzielczość ekranu", "system operacyjny"]]
        for j, label in enumerate(labels):
            label.grid(row=j, column=0)

        images1 = [ImageTk.PhotoImage(Image.open("{id}".format(id=data[i][5]))) for i in range(n)]
        images2 = [ImageTk.PhotoImage(Image.open("{id}".format(id=data[i][6]))) for i in range(n)]

        for i in range(n):

            image_frame = tk.Frame(window, width=100, height=200)
            image_frame.grid(row=0, column=i + 1)

            image_label1 = tk.Label(image_frame, image=images1[i])
            image_label1.grid(row=0, column=0)

            image_label2 = tk.Label(image_frame, image=images2[i])
            image_label2.grid(row=1, column=0)

            label_frame = tk.Frame(window, width=100, height=400)
            label_frame.grid(row=1, column=i + 1)

            labels = [tk.Label(label_frame, text="{data}".format(data=data[i][j])) for j in range(len(data[0]))]
            for j, label in enumerate(labels):
                label.grid(row=j, column=0)

        window.mainloop()
