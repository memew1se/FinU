package Collections1;

import java.util.*;

public class Coll {

    // Коллекция без дубликатов
    public static <T>Collection<T> noDuplicates(Collection<T> coll){
        return new HashSet<>(coll);
    }

    /**Реализовать метод, который добавляет 1_000_000 случайных элементов в ArrayList и
     LinkedList. Реализовать второй метод, который выбирает из списка элемент наугад 100_000
     раз. Замерьте время и скажите кто быстрее.
     */
    public static void timingTwoLists(){
        ArrayList<Double> arrayList = new ArrayList<>();
        LinkedList<Double> linkedList = new LinkedList<>();

        for (int i = 0; i < 1_000_000; i++){
            arrayList.add(Math.random());
            linkedList.add(Math.random());
        }

        long startTime = System.currentTimeMillis();
        for (int i = 0; i < 100_000; i++){
            arrayList.get((int)(Math.random() * (100_000 - 1)));
        }
        System.out.println(System.currentTimeMillis() - startTime);

        startTime = System.currentTimeMillis();
        for (int i = 0; i < 100_000; i++){
            linkedList.get((int)(Math.random() * (100_000 - 1)));
        }
        System.out.println(System.currentTimeMillis() - startTime);
    }

    // Частотный словарь слов
    public static void wordMap(String text){

        String[] words = text.replaceAll("\\p{Punct}", "").toLowerCase().split("\\s+");
        Map<String, Integer> map = new HashMap<>();

        for (String word: words){
            if (map.get(word) != null) {
                map.replace(word, map.get(word) + 1);
            } else {
                map.put(word, 1);
            }
        }
        System.out.println(map);
    }



}
