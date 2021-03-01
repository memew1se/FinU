package mark;

public class Atelier {

    public void WomanDress (Clothes[] clothes) {
        for (Clothes c: clothes) {
            if (c instanceof WomanClothes) {
                System.out.println("Женская одежда");
                System.out.println(c.size);
                System.out.println(c.price);
                System.out.println(c.color);
            }
        }
    }

    public void ManDress (Clothes[] clothes) {
        for (Clothes c: clothes) {
            if (c instanceof ManClothes) {
                System.out.println("Мужская одежда");
                System.out.println(c.size);
                System.out.println(c.price);
                System.out.println(c.color);
            }
        }
    }

}
