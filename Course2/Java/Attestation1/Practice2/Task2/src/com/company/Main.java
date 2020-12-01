package com.company;

import java.util.Random;

/*
Создайте класс, который описывает вектор (в трёхмерном пространстве).
У него должны быть:
    a. конструктор с параметрами в виде списка координат x, y, z

    b. метод, вычисляющий длину вектора. Корень можно посчитать с помощью
    Math.sqrt()

    c. метод, вычисляющий скалярное произведение

    d. метод, вычисляющий векторное произведение с другим вектором

    e. метод, вычисляющий угол между векторами (или косинус угла): косинус
    угла между векторами равен скалярному произведению векторов, деленному
    на произведение модулей (длин) векторов

    f. методы для суммы и разности

    g. статический метод, который принимает целое число N, и возвращает массив
    случайных векторов размером N

    h. Если метод возвращает вектор, то он должен возвращать новый объект, а не
    менять базовый
 */

class Vector {

    int x;
    int y;
    int z;

    public Vector(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public void coords() {
        System.out.printf("(%2d, %2d, %2d)%n", x, y, z);
    }

    // Длина вектора
    public double length() {
        return Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2) + Math.pow(z, 2));
    }

    // Скалярное произведение
    public double scalarProduct (Vector vector) {
        return x * vector.x + y * vector.y + z * vector.z;
    }

    // Векторное произведение
    public Vector vectorProduct(Vector vector) {
        int productX = y * vector.z - z * vector.y;
        int productY = z * vector.x - x * vector.z;
        int productZ = x * vector.y - y * vector.x;
        return new Vector(productX, productY, productZ);
    }

    // Косинус угла
    public double cos(Vector vector) {
        return scalarProduct(vector) / (length() * vector.length());
    }

    // Сумма векторов
    public Vector sum(Vector vector) {
        return new Vector(x + vector.x, y + vector.y, z + vector.z);
    }

    // Разность векторов
    public Vector diff(Vector vector) {
        return new Vector(x - vector.x, y - vector.y, z - vector.z);
    }

    // Генератор массива векторов длинной N
    public static Vector[] generate(int n) {
        Vector[] vectorArray;
        vectorArray = new Vector[n];
        for (int i = 0; i < n; i++) {
            Random random = new Random();

            int newX = random.nextInt(100);
            int newY = random.nextInt(100);
            int newZ = random.nextInt(100);

            vectorArray[i] = new Vector(newX, newY, newZ);
        }

        return vectorArray;
    }

}

public class Main {

    public static void main(String[] args) {

        System.out.println("Вектор A:");
        Vector vector1 = new Vector(2, 2, 8);
        vector1.coords();

        System.out.println("\nДлина вектора A: " + vector1.length() );

        System.out.println("\nВектор B:");
        Vector vector2 = new Vector(3, 2, 2);
        vector2.coords();

        System.out.println("\nСкалярное произведение векторов A и B: " + vector1.scalarProduct(vector2));

        System.out.println("\nВекторное  произведение векторов A и B:");
        Vector resultVector1 = vector1.vectorProduct(vector2);
        resultVector1.coords();

        System.out.println("\nКосинус угла векторов A и B: " + vector1.cos(vector2));

        System.out.println("\nСумма векторов A и B:");
        Vector resultVector2 = vector1.sum(vector2);
        resultVector2.coords();

        System.out.println("\nРазность векторов A и B:");
        Vector resultVector3 = vector1.diff(vector2);
        resultVector3.coords();

        System.out.println("\nМассив из 8 векторов:");
        Vector[] vectors = Vector.generate(8);
        for (Vector vector : vectors) {
            vector.coords();
        }
    }
}
