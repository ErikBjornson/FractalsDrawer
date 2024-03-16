import tkinter as tk
import random

class Application(tk.Tk):

    def __init__(self) -> None:

        self.__mem = [] # array for storing coordinates of points
        self.__size = 450 # window size

        super().__init__()
        self.title("Fractal")
        self.geometry(f"{self.__size}x{self.__size}")
        self.resizable(False, False)

        self.__canvas = tk.Canvas(
            background='black',
            width=self.__size - 4,
            height=self.__size - 4
        )
        self.__canvas.pack()
        self.__canvas.bind("<ButtonPress-1>", self.__pointHolder)
        self.__canvas.bind("<Double-ButtonPress-1>", self.__fractalizator)
    
    # function of iterational process
    def __fractalizator(self, event) -> None:
        # checking all points have been placed
        if len(self.__mem) <= 3: return
        for _ in range(5000):
            self.__generator()
            self.update()

    # function of generating new points and constructing fractal
    def __generator(self) -> None:
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
    def __pointHolder(self, event) -> None:
        # checking not all points have been placeds
        if(len(self.__mem)) > 3:
            return
        # function for determining the color of points
        Colorizer = lambda n: "red" if n < 3 else "green"
        # creating points
        self.__canvas.create_oval(
            event.x,
            event.y,
            event.x + 9,
            event.y + 9,
            outline = Colorizer(len(self.__mem)),
            fill='white', width=2)
        # memorizing coordinates of points
        self.__mem.append([event.x, event.y, event.x + 9, event.y + 9])
