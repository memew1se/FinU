package com.company;

import java.util.Random;

class Libra {

    int[] values;
    int[] scales;
    int[] array;

    public Libra (int[] values, int[] scales) {

        if (values.length != scales.length) {
            System.out.println("Длина массива значений должна равняться длине массива весов!");
            return;
        }

        this.values = values;
        this.scales = scales;

        int arrayLength = 0;

        for (int scale: scales) {
            arrayLength += scale;
        }

        array = new int[arrayLength];

        int i = 0;
        for (int k = 0; k < scales.length; k++) {
            int j = 0;
            while (j < scales[k]) {
                array[i] = values[k];
                i++;
                j++;
            }
        }
    }

    public void showArray() {
        for (int value: array) {
            System.out.print(value + " ");
        }
        System.out.println();
    }

    public int getNumber() {
        Random random = new Random();
        return array[random.nextInt(array.length)];
    }

}

public class Main {

    public static void main(String[] args) {

        int[] values = {1, 2, 3};
        int[] scales = {1, 2, 10};

	    Libra libra = new Libra(values, scales);
	    // libra.showArray();

	    int number = libra.getNumber();
        System.out.println("Возвращенный элемент: " + number);
    }
}
