package Collections2;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class MatrixIterator<T> implements Iterator<T> {

    private T[][] matrix;
    private final int elements;
    private int current_row = 0;
    private int current_column = 0;
    private int current_position = 0;

    public MatrixIterator(T[][] matrix) {
        this.elements = sizeOfMatrix(matrix);
        this.matrix = matrix;
    }

    public int sizeOfMatrix(T[][] matrix) {
        int elements = 0;
        for (T[] row :matrix){
            for (T column: row) {
                elements += 1;
            }
        }
        return elements;
    }

    @Override
    public boolean hasNext() {
        return elements > current_position;
    }

    @Override
    public T next() {
        if (!this.hasNext()) {
            System.out.println("Больше элементов нет");
            throw new NoSuchElementException();
        }

        T element = matrix[current_row][current_column];
        current_position++;
        current_column++;

        if (current_column >= matrix[current_row].length) {
            current_column = 0;
            current_row++;
        }
        return element;
    }

}

