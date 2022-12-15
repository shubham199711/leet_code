import java.util.ArrayList;

public class Main {

  public static void main(String[] args) {
    Controller ctl = new Controller();
    BaseMid newBase = new BaseMid(10);
    ToppingMushrooms topping1 = new ToppingMushrooms(100);
    ctl.addIngredient(newBase);
    ctl.addIngredient(topping1);
    System.out.println("Hello world!");
    System.out.println(ctl.getTotalPrice());
  }
}

abstract interface Ingredient {
  int getPrice();
}

class BaseMid implements Ingredient {
  int price;

  public BaseMid(int price) {
    this.price = price;
  }

  public BaseMid() {
    System.out.println("Please pass price");
  }

  public int getPrice() {
    return this.price;
  }
}

class ToppingMushrooms implements Ingredient {
  int price;
  float discount;

  public ToppingMushrooms(int price) {
    this.price = price;
    this.discount = 0.10f;
  }

  public ToppingMushrooms() {
    System.out.println("Please pass price");
  }

  public int getPrice() {
    return (int) ((float) this.price * (float) this.discount);
  }
}

class Controller {
  ArrayList<Ingredient> items = new ArrayList<Ingredient>();

  public void addIngredient(Ingredient newData) {
    this.items.add(newData);
  }

  public int getTotalPrice() {
    int total = 0;
    for (Ingredient num : this.items) {
      total += num.getPrice();
    }
    return total;
  }
}
