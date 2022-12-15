import abc


class Ingredient(abc.ABC):
    @abc.abstractclassmethod
    def getPrice() -> int:
        return 0


class BaseMid(Ingredient):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def getPrice(self) -> int:
        return self.value


class ToppingMushrooms(Ingredient):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value
        self.discount = 0.10

    def getPrice(self) -> int:
        return int(self.value * self.discount)


class PizzaController():
    def __init__(self) -> None:
        self.listOfTopping: list[Ingredient] = []

    def add_ingredient(self, item: Ingredient):
        self.listOfTopping.append(item)

    def get_total_price(self):
        return sum([x.getPrice() for x in self.listOfTopping])


if __name__ == "__main__":
    base_mid = BaseMid(10)
    topping_mushrooms = ToppingMushrooms(100)
    topping_mushrooms2 = ToppingMushrooms(100)
    clt = PizzaController()
    clt.add_ingredient(base_mid)
    clt.add_ingredient(topping_mushrooms)
    clt.add_ingredient(topping_mushrooms2)
    print(clt.get_total_price())
