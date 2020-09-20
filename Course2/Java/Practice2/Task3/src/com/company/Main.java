package com.company;

class Shape {

    double volume;

    public Shape(double volume) {
        this.volume = volume;
    }

    public double getVolume() {
        return volume;
    }
}

class SolidOfRevolution extends Shape {

    double radius;

    public SolidOfRevolution(double volume, double radius) {
        super(volume);
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }
}

class Ball extends SolidOfRevolution {
    public Ball(double radius) {
        super(Math.PI * Math.pow(radius, 3) * 4 / 3, radius);
    }
}

class Cylinder extends SolidOfRevolution {

    double height;

    public Cylinder(double radius, double height) {
        super(Math.PI * Math.pow(radius, 2) * height, radius);
        this.height = height;
    }
}

class Pyramid extends Shape{

    double height;
    double s;

    public Pyramid(double height, double s) {
        super(height * s / 3);
        this.height = height;
        this.s = s;
    }
}

class Box extends Shape {

    double space;

    public Box(double space) {
        super(space);
        this.space = space;
    }

    public boolean add(Shape shape) {
        if (space >= shape.getVolume()) {
            space -= shape.getVolume();
            return true;
        }
        else {
            return false;
        }
    }

    public double getSpace() {
        return space;
    }
}

public class Main {

    public static void main(String[] args) {

	    Box box = new Box(1000);
	    Ball ball = new Ball(5);

        System.out.println("Начальный объем: " + box.getSpace());

        System.out.println("\nДобавляем шар с объемом " + ball.getVolume());
	    box.add(ball);
        System.out.println("Оставшийся объем: " + box.getSpace());

        System.out.println("\nПытаемся добаить тот же шар еще раз");
        System.out.println("Результат: " + box.add(ball));
        System.out.println("Оставшийся объем: " + box.getSpace());

        Pyramid pyramid = new Pyramid(10, 30);

        System.out.println("\nДобавляем пирамидку с объемом " + pyramid.getVolume());
        box.add(pyramid);
        System.out.println("Оставшийся объем: " + box.getSpace());

    }
}
