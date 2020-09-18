from tkinter import *
import math


class Application(Canvas):
    def __init__(self, master, **options):
        super().__init__(master, **options)
        self.grid()
        self.update()

        self.update_time = 1

        # Координаты центра
        self.center_x = self.winfo_width() // 2
        self.center_y = self.winfo_height() // 2

        # Параметры круга
        self.circle_radius = 200
        self.circle_coords = [self.center_x - self.circle_radius,  # x1
                              self.center_y - self.circle_radius,  # y1

                              self.center_x + self.circle_radius,  # x2
                              self.center_y + self.circle_radius]  # y2

        # Параметры точки
        self.current_angle = 0
        self.current_speed = 0.001
        self.point_radius = 5
        self.point_coords = [self.center_x + self.circle_radius - self.point_radius,  # x1
                             self.center_y - self.point_radius,                       # y1

                             self.center_x + self.circle_radius + self.point_radius,  # x2
                             self.center_y + self.point_radius]                       # y2

        self.create_widgets()
        self.animation()

    def create_widgets(self):
        # Создаем круг
        self.create_oval(*self.circle_coords, fill="#CD5C5C", tag="circle")

        # Создаем точку
        self.create_oval(*self.point_coords, fill="#FFA07A", tag="point")

    def animation(self):
        self.current_angle += self.current_speed

        new_x = self.center_x + self.circle_radius * math.sin(self.current_angle)
        new_y = self.center_y + self.circle_radius * math.cos(self.current_angle)

        x1 = new_x - self.point_radius
        y1 = new_y - self.point_radius
        x2 = new_x + self.point_radius
        y2 = new_y + self.point_radius
        
        self.coords("point", x1, y1, x2, y2)
        self.after(self.update_time, self.animation)


if __name__ == '__main__':
    root = Tk()
    root.title("Laboratory 0")
    app = Application(root, width=600, height=600, bg="#292626")
    root.mainloop()
