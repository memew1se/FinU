package com.company;

import java.util.Random;

/*
Реализуйте класс матрицы и методы
a. Сложение и вычитание матриц.
b. Умножение матрицы на число.
c. Произведение двух матриц.
d. Транспонированная матрица.
e. Возведение матрицы в степень.
f. Если метод, возвращает матрицу, то он должен возвращать новый объект, а не менять базовый.
 */

class Matrix {

    private int line;
    private int column;
    private long[][] thisMatrix;

    // Конструктор неготовой матрицы
    public Matrix(int line, int column) {

        // Проверка на входные значения
        if (line <= 0 | column <= 0) {
            System.out.println("Значения должны быть больше нуля!");
            return;
        }

        this.line = line;
        this.column = column;
        this.thisMatrix = new long[line][column];

        Random random = new Random();
        for (int i = 0; i < line; i++) {
            for (int j = 0; j < column; j++) {
                thisMatrix[i][j] = random.nextInt(100);
            }
        }
    }

    // Конструктор готовой матрицы
    public Matrix(long[][] thisMatrix) {

        this.line = thisMatrix.length;
        this.column = thisMatrix[0].length;
        this.thisMatrix = thisMatrix;
    }

    // Вывод матрицы на экран
    public void show() {

        for (int i = 0; i < line; i++) {
            for (int j = 0; j < column; j++) {
                System.out.print(" " + thisMatrix[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    // Умножение матрицы на число
    public Matrix multiplication(int number) {

        long[][] multiplicatedMatrix = new long[line][column];

        for (int i = 0; i < line; i++) {
            for (int j = 0; j < column; j++) {
                multiplicatedMatrix[i][j] = thisMatrix[i][j] * number;
            }
        }
        return new Matrix(multiplicatedMatrix);
    }

    // Умножение матрицы на матрицу
    public Matrix multiplication(Matrix matrix) {

        if (column != matrix.line) {
            System.out.println("Матрицы не согласованы!");
            return null;
        }

        long[][] factorMatrix = matrix.thisMatrix;
        long[][] compositionMatrix = new long[line][matrix.column];

        for (int i = 0; i < line; i++) {
            for (int j = 0; j < matrix.column; j++) {
                int sum = 0;
                for (int k = 0; k < column; k++) {
                    sum += thisMatrix[i][k] * factorMatrix[k][j];
                }
                compositionMatrix[i][j] = sum;
            }
        }
        return new Matrix(compositionMatrix);
    }

    // Транспонирование матрицы
    public Matrix transpose() {

        long[][] transposedMatrix = new long[column][line];

        for (int i = 0; i < line; i++) {
            for (int j = 0; j < column; j++) {
                transposedMatrix[j][i] = thisMatrix[i][j];
            }
        }
        return new Matrix(transposedMatrix);
    }

    // Возведение матрицы в степень
    public Matrix power(int degree) {

        if (line != column) {
            System.out.println("Матрица должна быть квадратной!");
            return null;
        }

        Matrix cloneMatrix = new Matrix(thisMatrix);
        Matrix poweredMatrix = new Matrix(thisMatrix);

        for (int i = 1; i < degree; i++) {
            poweredMatrix = poweredMatrix.multiplication(cloneMatrix);
        }
        return poweredMatrix;
    }

}

public class Main {

    public static void main(String[] args) {

        System.out.println("Матрица A:");
        Matrix matrix1 = new Matrix(3, 2);
        matrix1.show();

        System.out.println("Результат умножения матрицы A на число 2:");
        Matrix resultMatrix1 = matrix1.multiplication(2);
        resultMatrix1.show();

        System.out.println("Матрица B:");
        Matrix matrix2 = new Matrix(2, 4);
        matrix2.show();

        System.out.println("Результат умножения матрицы A на матрицу B:");
        Matrix resultMatrix2 = matrix1.multiplication(matrix2);
        resultMatrix2.show();

        System.out.println("Транспонированная матрица B:");
        Matrix resultMatrix3 = matrix2.transpose();
        resultMatrix3.show();

        System.out.println("Матрица C:");
        Matrix matrix3 = new Matrix(2, 2);
        matrix3.show();

        System.out.println("Матрица C в 3 степени:");
        Matrix resultMatrix4 = matrix3.power(3);
        resultMatrix4.show();

    }
}
