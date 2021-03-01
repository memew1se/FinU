package mark;

public class Main {

    public static void main(String[] args) {

        ClothesSize.Sizes xxs = ClothesSize.Sizes.XXS;
        System.out.println(xxs.getDescription());

        ClothesSize.Sizes m = ClothesSize.Sizes.M;
        System.out.println(m.getDescription());

        Clothes pants = new Pants(32, 1000, "BLACK");
        Clothes shirt = new Shirt(34, 2000, "WHITE");
        Clothes skirt = new Skirt(35, 2030, "YELLOW");
        Clothes tie = new Tie(37, 2030, "Blue");


    }
}
