from tkinter import *
import math


class Application(Canvas):
    def __init__(self, master, **options):
        super().__init__(master, **options)
        self.pack()
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
        self.speed_multiplication = 1
        self.point_direction = 1
        self.point_radius = 10
        self.point_coords = [self.center_x + self.circle_radius - self.point_radius,  # x1
                             self.center_y - self.point_radius,  # y1

                             self.center_x + self.circle_radius + self.point_radius,  # x2
                             self.center_y + self.point_radius]  # y2

        self.create_widgets()
        self.animation()

    def create_widgets(self):
        # Создаем круг
        self.create_oval(*self.circle_coords, fill="#CD5C5C", tag="circle")

        # Создаем точку
        self.create_oval(*self.point_coords, fill="#FFA07A", tag="point")

        # Создаем кнопки
        self.exit_button = Button(self, text="Quit", command=self.quit, anchor=NW)
        self.exit_button.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        exit_window = self.create_window(10, 10, anchor=NW, window=self.exit_button)

        self.direction_button = Button(self, text="Против часовой", command=self.change_direction,
                                       anchor=NW)
        self.direction_button.configure(width=13, activebackground="#33B5E5", relief=FLAT)
        direction_window = self.create_window(100, 10, anchor=NW, window=self.direction_button)

        # Создаем шкалу
        self.speed_scale = Scale(self, orient=VERTICAL, length=100, from_=1, to=3,
                                 command=self.scale_update)
        self.speed_scale.set(2)
        speed_window = self.create_window(40, 100, window=self.speed_scale)

    def animation(self):
        self.current_angle += self.current_speed * self.point_direction * self.speed_multiplication
        self.current_angle %= 2 * math.pi

        new_x = self.center_x + self.circle_radius * math.cos(self.current_angle)
        new_y = self.center_y - self.circle_radius * math.sin(self.current_angle)

        x1 = new_x - self.point_radius
        y1 = new_y - self.point_radius
        x2 = new_x + self.point_radius
        y2 = new_y + self.point_radius

        self.coords("point", x1, y1, x2, y2)
        self.after(self.update_time, self.animation)

    def change_direction(self):
        self.point_direction *= (-1)

        if self.point_direction > 0:
            self.direction_button.configure(text="Против часовой")
        else:
            self.direction_button.configure(text=f"{'По часовой': ^19}")

    def scale_update(self, value):
        if int(value) == 1:
            self.speed_multiplication = 1/2
        elif int(value) == 2:
            self.speed_multiplication = 1
        else:
            self.speed_multiplication = 1.2


if __name__ == '__main__':
    root = Tk()
    root.title("Laboratory 0")
    app = Application(root, width=600, height=600, bg="#292626")
    root.mainloop()

