package Collections2;

import java.util.Iterator;

public class Main {

    public static void main(String[] args) {

        Integer[][] matrix = {{1,2,3},{4,5,6},{7,8,9}};
        MatrixIterator<Integer> iterator = new MatrixIterator<Integer>(matrix);

        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }


    }

}
