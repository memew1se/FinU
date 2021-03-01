package com.company;

abstract class Shape {

    public abstract double getVolume();
}

abstract class SolidOfRevolution extends Shape {

    double radius;

    public SolidOfRevolution(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }
}

class Ball extends SolidOfRevolution {

    public Ball(double radius) {
        super(radius);
    }

    @Override
    public double getVolume() {
        return Math.PI * Math.pow(radius, 3) * 4 / 3;
    }
}

class Cylinder extends SolidOfRevolution {

    double height;

    public Cylinder(double radius, double height) {
        super(radius);
        this.height = height;
    }

    @Override
    public double getVolume() {
        return Math.PI * Math.pow(radius, 2) * height;
    }
}

class Pyramid extends Shape{

    double height;
    double s;

    public Pyramid(double height, double s) {
        this.height = height;
        this.s = s;
    }

    @Override
    public double getVolume() {
        return height * s / 3;
    }
}

class Box extends Shape {

    double space;
    double volume;

    public Box(double space) {
        this.volume = space;
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

    @Override
    public double getVolume() {
        return volume;
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
