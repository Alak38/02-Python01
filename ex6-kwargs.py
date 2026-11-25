#!/usr/bin/python3
from typing import Any


class Plant:
    def __init__(self, nm: str, hgt: float, ag: int, hlth: int) -> None:
        """ Instantiate the object with the given values """
        self.name = nm
        self._height = hgt
        self._days = ag
        self.health = hlth
        self.stat = self.Statistics()

    @classmethod
    def anonymous(cls, **kwargs: Any) -> "Plant":
        """ set default values so that an object can be created with
        incomplete parameters
        """
        name = kwargs.get("name", "Unknown plant")
        height = kwargs.get("height", 0.0)
        age = kwargs.get("age", 0)
        health = kwargs.get("health", 50)
        return (cls(name, height, age, health))

    def show(self) -> None:
        """ Print infos about the plant """
        print(f"{self.name.capitalize()}: {self._height}", end="")
        print(f"cm, {self._days} days old")
        self.stat.add_show()

    def grow(self, nb_day: int = 7) -> float:
        """ Simulate the growth of the plant for n days (default 7) """
        self.stat.add_grow()
        growrate = 0.975 + (self.health * 0.0005)
        if self.health * 2 < self._days:
            growrate = 0.95
        elif self.health < self._days:
            growrate = 0.975
        base = self._height
        for x in range(1, nb_day + 1):
            self._height = round(self._height * growrate, 1)
            self._days += 1
        return (round(self._height - base, 1))

    def age(self, nb_day: int = 7) -> float:
        """ Simulate the aging of the plant for n days (default 7) """
        self.stat.red_grow()
        self.stat.add_age()
        return (self.grow(nb_day))

    def get_height(self) -> float:
        """ Return the actual height of the plant """
        return (self._height)

    def get_age(self) -> int:
        """ Return the actual age of the plant """
        return (self._days)

    def set_height(self, new_h: float) -> None:
        """ Set the height of the plant to a new value """
        if new_h < 0:
            print("Error, height can't be negative\nHeight update rejected")
        else:
            self._height = round(new_h, 1)
            print(f"Height updated: {self._height}")

    def set_age(self, new_d: int) -> None:
        """ Set the age of the plant to a new value """
        if new_d < 0:
            print("Error, age can't be negative\nAge update rejected")
        else:
            self._days = round(new_d, 1)
            print(f"Age updated: {self._days}")

    @staticmethod
    def year_check(nb_day: int) -> bool:
        """ Return if nb_day is more than a year or not """
        if nb_day >= 365:
            return (True)
        else:
            return (False)

    class Statistics:
        """ Stores stats about how many time show, grow, age
            and shade methods were called
        """
        def __init__(self) -> None:
            """ Instantiate the object "Statistics" with all values to 0"""
            self.__show = 0
            self.__grow = 0
            self.__age = 0
            self.__shade = 0

        def add_grow(self) -> None:
            """ Incrementes grow """
            self.__grow += 1

        def red_grow(self) -> None:
            """ Decrementes grow (for age() purpose) """
            self.__grow -= 1

        def add_show(self) -> None:
            """ Incrementes show """
            self.__show += 1

        def add_age(self) -> None:
            """ Incrementes age """
            self.__age += 1

        def add_shade(self) -> None:
            """ Incrementes shade """
            self.__shade += 1

        def display(self, tree: bool) -> None:
            """ Print the statistics (print shade only when needed) """
            print(f"Stats: {self.__grow} grow, {self.__age}", end="")
            print(f" age, {self.__show} show")
            if tree == 1:
                print(f" {self.__shade} shade")


class Flower(Plant):
    def __init__(self, nm: str, hgt: float, ag: int,
                 hlth: int, color: str) -> None:
        """ Instantiate the object with the given values
        (calls the Plant method)
        """
        super().__init__(nm, hgt, ag, hlth)
        self.color = color
        self.blm = 0

    def show(self) -> None:
        """ Print infos about the Flower (calls the Plant method) """
        super().show()
        print(f" Color: {self.color}")
        if self.blm == 0:
            print(f" {self.name.capitalize()} has not bloomed yet")
        if self.blm == 1:
            print(f" {self.name.capitalize()} is blooming beautifully!")

    def bloom(self) -> None:
        """ Makes the Flower bloom """
        if self.blm == 0:
            self.blm = 1


class Tree(Plant):
    def __init__(self, nm: str, hgt: float, ag: int,
                 hlth: int, diam: float) -> None:
        """ Instantiate the object with the given values
        (calls the Plant method)
        """
        super().__init__(nm, hgt, ag, hlth)
        self.trunk_diam = round(diam, 1)

    def show(self) -> None:
        """ Print infos about the Tree (calls the Plant method) """
        super().show()
        print(f" Trunk diameter: {self.trunk_diam}cm")

    def produce_shade(self) -> None:
        """ Make the Tree produces shades """
        print(f"Tree {self.name} now produces a shade of ", end="")
        print(f"{self._height}cm long and ", end="")
        print(f"{round(self.trunk_diam, 1)}cm wide.")
        self.stat.add_shade()


class Vegetable(Plant):
    def __init__(self, nm: str, hgt: float, ag: int,
                 hlth: int, harv: str) -> None:
        """ Instantiate the object with the given values
        (calls the Plant method)
        """
        super().__init__(nm, hgt, ag, hlth)
        self.harvest = harv
        self.nut_val = 0

    def show(self) -> None:
        """ Print infos about the Vegetable (calls the Plant method) """
        super().show()
        print(f" Harvest season: {self.harvest}")
        print(f" Nutritionnal value: {self.nut_val}")

    def grow(self, nb_day: int = 7) -> float:
        """ Simulate the growth of the Vegetable for n days (default 7)
        calls the Plant method)
        """
        self.nut_val += 1
        return (super().grow(nb_day))

    def age(self, nb: int = 7) -> float:
        """ Simulate the age of the Vegetable for n days (default 7)
        calls the Plant method)
        """
        self.nut_val += 1
        return (super().grow(nb))


class Seed(Flower):
    def __init__(self, nm: str, hgt: float, ag: int,
                 hlth: int, color: str) -> None:
        """ Instantiate the object with the given values
        (calls the Flower method)
        """
        super().__init__(nm, hgt, ag, hlth, color)
        self.n_seed = 0

    def bloom(self) -> None:
        """ Makes the Flower bloom """
        super().bloom()
        self.n_seed += 42

    def show(self) -> None:
        """ Print infos about the Seed (calls the Flower & Plant method) """
        super().show()
        print(f" Seeds: {self.n_seed}")


def display_stats(pl: Plant, clas: str) -> None:
    """ Display the statistics about the object given in parameters"""
    print(f"[statistics for {pl.name.capitalize()}]")
    if (clas == "Tree"):
        pl.stat.display(True)
    else:
        pl.stat.display(False)


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year old")
    n = 30
    print(f"Is {n} days more than a year? -> {Plant.year_check(n)}")
    n = 400
    print(f"Is {n} days more than a year? -> {Plant.year_check(n)}\n")
    print("=== Flower")
    p1 = Flower("rose", 15.0, 10, 90, "red")
    p1.show()
    display_stats(p1, "Flower")
    print(f"[asking the {p1.name} to grow and bloom]")
    p1.grow(7)
    p1.bloom()
    p1.show()
    display_stats(p1, "Flower")
    print("\n=== Tree")
    p2 = Tree("oak", 200.0, 365, 70, 5)
    p2.show()
    display_stats(p2, "Tree")
    print(f"[asking the {p2.name} to produce shade]")
    p2.produce_shade()
    display_stats(p2, "Tree")
    print("\n=== Seed")
    p3 = Seed("sunflower", 80.0, 45, 80, "yellow")
    p3.show()
    print(f"[make {p3.name} grow, age and bloom]")
    p3.grow(10)
    p3.age(10)
    p3.bloom()
    p3.show()
    display_stats(p3, "Seed")
    # print("\n=== Vegetable")
    # p3 = Vegetable("tomato", 5.0, 10, 75, "April").show()
    # nb = 20
    # print(f"[make {p3.name} grow and age for {nb}]")
    # p3.grow(20)
    # p3.show()
    # p4 = Plant.anonymous(name="mysterious Plant", height=42.42)
    print("\n=== Anonymous")
    p4 = Plant.anonymous()
    p4.show()
    display_stats(p4, "Anonymous")
