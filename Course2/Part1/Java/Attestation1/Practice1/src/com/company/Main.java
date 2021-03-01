package com.company;

public class Main {

    public static double distance(double x1, double y1, double x2, double y2) {
        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
    }

    public static double geometricAverage(int value1, int value2) {
        return Math.sqrt(value1 * value2);
    }

    public static double arithmeticAverage(int value1, int value2) {
        return (value1 + value2) / 2;
    }

    public static int minus21(int number) {
        return number - 21;
    }

    public static void main(String[] args) {
	    // 1. Выведите на экран текст Hello World
        System.out.println("Hello World");

        // 2. Создайте переменную, присвойте ей целочисленное значение. Выведите значение на экран
        int variable1 = 69;
        System.out.println(variable1);

        // 3. Создайте переменную, увеличьте ее на единицу несколькими способами и выведите значение на экран
        int variable2 = 420;

        ++variable2;
        System.out.println(variable2);

        variable2++;
        System.out.println(variable2);

        variable2 += 1;
        System.out.println(variable2);

        // 4. Даны две переменные. Поменяйте значения переменных друг с другом двумя способами
        int x = 4;
        int y = 2;
        System.out.println("x = " + x + " y = " + y);

        int buffer = x;
        x = y;
        y = buffer;
        System.out.println("x = " + x + " y = " + y);

        x = x + y - (y=x);
        System.out.println("x = " + x + " y = " + y);

        // 5. Дано два числа x и y. Найдите гипотенузу треугольника с заданными катетами
        long a = 3;
        long b = 4;
        System.out.println("Гипотенуза равна " + Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2)));

        // 6. Дано натуральное число. Выведите его последнюю цифру
        long value1 = 42069;
        System.out.println(value1 % 10);

        // 7. Дано неотрицательное целое число. Найдите число десятков в его десятичной записи
        long value2 = 69420;
        System.out.println(value2 % 100 / 10);

        // 8. Дано двузначное число. Найдите число десятков в нем
        long value3 = 42;
        System.out.println(value3 / 10);

        // 9. Реализуйте метод, который получает целое число на вход и возвращает разницу между данным числом и 21.
        // Выведите значение на экран с различными целыми числами
        System.out.println(minus21(42));
        System.out.println(minus21(69));
        System.out.println(minus21(420));


        // 10. Реализуйте метод, в который передается две целочисленные переменные и возвращает их среднее арифметическое
        System.out.println(arithmeticAverage(10, 20));
        System.out.println(arithmeticAverage(65, 145));
        System.out.println(arithmeticAverage(1000, 1000));

        // 11. Реализуйте метод, в который передается две целочисленные переменные и возвращает их среднее геометрическое
        System.out.println(geometricAverage(8, 8));
        System.out.println(geometricAverage(9, 12));
        System.out.println(geometricAverage(4, 36));

        // 12. Реализуйте метод, в который передается 4 числа с плавающей точкой. Первые два числа – координаты x, y первой точки.
        // Вторые два числа – координаты x,y второй точки. Найти расстояние между двумя точками
        System.out.println(distance(1.0, 1.0, 2.0, 2.0));
        System.out.println(distance(13.1, 15.0, 25.5, 32.0));
        System.out.println(distance(16.0, 22.6, 2.0, 221.3));

    }
}
