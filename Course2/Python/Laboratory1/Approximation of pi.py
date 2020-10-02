from tkinter import *
import math

import random


class Application(Canvas):
    def __init__(self, master, **options):
        super().__init__(master, **options)
        self.grid()
        self.update()

        self.amount_of_points_in_circle = 0

        # Координаты центра
        self.center_x = self.winfo_width() // 2
        self.center_y = self.winfo_height() // 2

        # Параметры круга
        self.circle_radius = 100
        self.circle_coords = [self.center_x - self.circle_radius,  # x1
                              self.center_y - self.circle_radius,  # y1

                              self.center_x + self.circle_radius,  # x2
                              self.center_y + self.circle_radius]  # y2

        self.all_coords = []
        self.all_circle_coords = []

        for x in range(-self.winfo_width() - 4, self.winfo_width() + 3, 4):
            for y in range(-self.winfo_height() - 4, self.winfo_height() + 3, 4):

                if math.sqrt(x**2+y**2) <= self.circle_radius:
                    self.all_circle_coords.append((x, y))
                else:
                    self.all_coords.append((x, y))

        # Параметры кнопок
        self.exit_button = Button(self,
                                  text="Quit",
                                  command=self.quit,
                                  anchor=NW)

        self.exit_button.configure(width=10,
                                   activebackground="#33B5E5",
                                   relief=FLAT)

        self.label = Label(self)

        self.create_widgets()
        self.animation()

    def create_widgets(self):
        # Создаем круг
        self.create_oval(*self.circle_coords, fill="black", outline="orange", tag="circle")

        # Создаем кнопки
        self.create_window(10, 10, anchor=NW, window=self.exit_button)

        # Создаем метку
        self.create_window(100, 13, anchor=NW, window=self.label)

    def animation(self):
        try:
            index = random.randint(0, len(self.all_circle_coords) - 1)

            x, y = self.all_circle_coords[index]

            self.amount_of_points_in_circle += 16
            self.create_oval(self.center_x + x - 3, self.center_y + y - 3,
                             self.center_x + x + 3, self.center_y + y + 3,

                             fill="orange", outline="orange")

            del (self.all_circle_coords[index])
        except ValueError:
            pass

        try:
            index = random.randint(0, len(self.all_coords) - 1)

            x, y = self.all_coords[index]

            self.create_oval(self.center_x + x - 2, self.center_y + y - 2,
                             self.center_x + x + 2, self.center_y + y + 2,

                             fill="#00B454", outline="#00B454")

            del (self.all_coords[index])
        except ValueError:
            pass

        self.label_update()

        self.after(1, self.animation)

    def label_update(self):
        pi = self.amount_of_points_in_circle * self.circle_radius ** (-2)
        self.label.configure(text="Approximated value: {:.4f}".format(pi))


if __name__ == '__main__':
    root = Tk()
    root.title("Laboratory 1")
    app = Application(root, width=600, height=600, bg="black")
    root.mainloop()
