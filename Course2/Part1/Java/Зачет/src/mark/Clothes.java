package mark;

public abstract class Clothes {

    public int size;
    public int price;
    public String color;

    Clothes() {
    }
}

class Shirt extends Clothes implements ManClothes, WomanClothes {

    public int size;
    public int price;
    public String color;

    Shirt(int size, int price, String color) {
        this.size = size;
        this.price = price;
        this.color = color;
    }

    @Override
    public void DressMan() {
        System.out.println("Футболка надета");
    }

    @Override
    public void DressWoman() {
        System.out.println("Футболка надета");
    }

}

class Pants extends Clothes implements ManClothes, WomanClothes {

    public int size;
    public int price;
    public String color;

    Pants(int size, int price, String color) {
        this.size = size;
        this.price = price;
        this.color = color;
    }

    @Override
    public void DressMan() {
        System.out.println("Футболка надета");
    }

    @Override
    public void DressWoman() {
        System.out.println("Футболка надета");
    }

}

class Skirt extends Clothes implements WomanClothes {

    public int size;
    public int price;
    public String color;

    Skirt(int size, int price, String color) {
        this.size = size;
        this.price = price;
        this.color = color;
    }

    @Override
    public void DressWoman() {
        System.out.println("Футболка надета");
    }

}

class Tie extends Clothes implements ManClothes {

    public int size;
    public int price;
    public String color;

    Tie(int size, int price, String color) {
        this.size = size;
        this.price = price;
        this.color = color;
    }

    @Override
    public void DressMan() {
        System.out.println("Футболка надета");
    }

}