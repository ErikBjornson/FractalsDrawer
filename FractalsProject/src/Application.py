import tkinter as tk
import random

class Application(tk.Tk):

    def __init__(self):

        self.__mem = [] # array for storing coordinates of points
        self.__size = 450 # window size
        self.__flag = True # point placement blocker

        super().__init__()
        self.title("Fractal")
        self.geometry(f"{self.__size}x{self.__size}")
        self.resizable(False, False)

        main_menu = tk.Menu(self)
        main_menu.add_command(label="Start", command=self.__fractalizator)
        self.config(menu=main_menu)

        self.__canvas = tk.Canvas(
            background='black',
            width=self.__size - 4,
            height=self.__size - 4
        )
        self.__canvas.pack()
        self.__canvas.bind("<Button-1>", self.__pointHolder)
    
    # function of iterational process
    def __fractalizator(self):
        # checking the first and last press of the start button has been made
        if len(self.__mem) != 4 or not self.__flag:
            return
        self.__flag = False
        for _ in range(5000):
            self.__generator()
            self.update()

    # function of generating new points and constructing fractal
    def __generator(self):
        r = random.randint(0, 2)
        new_point = self.__canvas.create_oval(
            (self.__mem[-1][0] + self.__mem[r][0]) // 2,
            (self.__mem[-1][1] + self.__mem[r][1]) // 2,
            (self.__mem[-1][2] + self.__mem[r][2]) // 2 - 3,
            (self.__mem[-1][3] + self.__mem[r][3]) // 2 - 3,
            fill='white', outline='white'
        )
        self.__mem[-1] = self.__canvas.coords(new_point)

    # function of click-event
    def __pointHolder(self, event):
        # creating three reference points
        if len(self.__mem) < 3:
            self.__canvas.create_oval(
                    event.x,
                    event.y,
                    event.x + 9,
                    event.y + 9,
                    outline='red', fill='white', width=2)
        # creating a starting point
        elif len(self.__mem) == 3:
            self.__canvas.create_oval(
                    event.x,
                    event.y,
                    event.x + 9,
                    event.y + 9,
                    outline='green', fill='white', width=2)
        else:
            return
        # memorizing coordinates of points
        self.__mem.append([event.x, event.y, event.x + 9, event.y + 9])
