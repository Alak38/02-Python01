#!/usr/bin/python3

class Plant:
    def __init__(self: Plant, nm: str, hgt: float, ag: int, hlth: int) -> None:
        self.name = nm
        self._height = hgt
        self._days = ag
        self.health = hlth

    def show(self: Plant) -> Plant:
        print(f"{self.name.capitalize()}: {self._height}", end="")
        print(f"cm, {self._days} days old")
        return (self)

    def grow(self: Plant) -> float:
        growrate = 0.975 + (self.health * 0.0005)
        if self.health * 2 < self._days:
            growrate = 0.95
        elif self.health < self._days:
            growrate = 0.975
        base = self._height
        self._height = round(self._height * growrate, 1)
        self._days += 1
        return (round(self._height - base, 1))

    def age(self: Plant) -> float:
        return (self.grow())

    def get_height(self: Plant) -> float:
        return (self._height)

    def get_age(self: Plant) -> int:
        return (self._days)

    def set_height(self: Plant, new_h: float) -> None:
        if new_h < 0:
            print("Error, height can't be negative\nHeight update rejected")
        else:
            self._height = round(new_h, 1)
            print(f"Height updated: {self._height}")

    def set_age(self: Plant, new_d: int) -> None:
        if new_d < 0:
            print("Error, age can't be negative\nAge update rejected")
        else:
            self._days = round(new_d, 1)
            print(f"Age updated: {self._days}")


class Flower(Plant):
    def __init__(self: Flower, nm: str, hgt: float, ag: int,
                 hlth: int, color: str) -> None:
        super().__init__(nm, hgt, ag, hlth)
        self.color = color
        self.blm = 0

    def show(self: Flower) -> Flower:
        super().show()
        print(f" Color: {self.color}")
        if self.blm == 0:
            print(f" {self.name.capitalize()} has not bloomed yet")
        if self.blm == 1:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        return (self)

    def bloom(self: Flower) -> None:
        if self.blm == 0:
            self.blm = 1


class Tree(Plant):
    def __init__(self: Tree, nm: str, hgt: float, ag: int,
                 hlth: int, diam: float) -> None:
        super().__init__(nm, hgt, ag, hlth)
        self.trunk_diam = round(diam, 1)

    def show(self: Tree) -> Tree:
        super().show()
        print(f" Trunk diameter: {self.trunk_diam}cm")
        return (self)

    def produce_shade(self: Tree) -> None:
        print(f"Tree {self.name} now produces a shade of {self._height}cm")
        print(f" long and {round(self.trunk_diam, 1)}cm wide")


class Vegetable(Plant):
    def __init__(self: Vegetable, nm: str, hgt: float, ag: int,
                 hlth: int, harv: str) -> None:
        super().__init__(nm, hgt, ag, hlth)
        self.harvest = harv
        self.nut_val = 0

    def show(self: Vegetable) -> Vegetable:
        super().show()
        print(f" Harvest season: {self.harvest}")
        print(f" Nutritionnal value: {self.nut_val}")
        return (self)

    def grow(self: Vegetable) -> float:
        self.nut_val += 1
        return (super().grow())

    def age(self: Vegetable) -> float:
        self.nut_val += 1
        return (super().grow())


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    p1 = Flower("rose", 15.0, 10, 30, "red")
    p1.show()
    print(f"[asking the {p1.name} to bloom]")
    p1.bloom()
    p1.show()
    print("\n=== Tree")
    p2 = Tree("oak", 200.0, 365, 70, 5).show()
    print(f"[asking the {p2.name} to produce shade]")
    p2.produce_shade()
    print("\n=== Vegetable")
    p3 = Vegetable("tomato", 5.0, 10, 75, "April").show()
    nb = 20
    print(f"[make {p3.name} grow and age for {nb} days]")
    for x in range(1, nb + 1):
        p3.grow()
    p3.show()
