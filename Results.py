import tkinter as tk


class results:
    def __init__(self,ranking,inconsitancies): #TODO display ranking of computers, and inconsistancies of matrixes
        window = tk.Tk()

        window.geometry("400x400")

        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1,
        )

        label = tk.Label(master=frame, text="Ranking: ")
        label.pack()

        frame.pack()

        window.mainloop()


if __name__ == "__main__":
    t = results()
