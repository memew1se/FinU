package Collections1;

import java.util.*;

public class Main {

    public static void main(String[] args) {

        ArrayList<Integer> array = new ArrayList<>();
        for (int i = 0; i < 10; i++){
            array.add(i % 2);
        }

        System.out.println(array);
        System.out.println(Coll.noDuplicates(array));

        System.out.println("--------");

        Coll.timingTwoLists();

        System.out.println("--------");

        String text = "Что в космосе тебе нравится больше всего? Мне космос. Космос. Космос не может ждать.";

        Coll.wordMap(text);

    }
}
