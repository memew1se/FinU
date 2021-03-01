package wikimedia;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws Exception {
        System.out.println("Введите тему запроса или нажмите enter для выхода!");

        Scanner in = new Scanner(System.in);
        String target;

        while (true){
            System.out.print("\nВведите тему: ");
            target = in.nextLine();
            if(target.equals("")){
                System.out.println("До свидания!");
                break;
            }
            Parser parse = new Parser(target);
        }
    }
}
