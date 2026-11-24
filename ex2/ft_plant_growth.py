#!/usr/bin/python3

class Plant:
    def __init__(self: Plant, nm: str, hgt: float, ag: int, hlth: int) -> None:
        self.name = nm
        self.height = hgt
        self.days = ag
        self.health = hlth

    def show(self: Plant) -> None:
        print(f"{self.name.capitalize()}: {self.height}", end="")
        print(f"cm, {self.days} days old")

    def grow(self: Plant) -> float:
        growrate = 0.975 + (self.health * 0.0005)
        if self.health * 2 < self.days:
            growrate = 0.95
        elif self.health < self.days:
            growrate = 0.975
        base = self.height
        self.height = round(self.height * growrate, 1)
        self.days += 1
        return (round(self.height - base, 1))

    def age(self: Plant) -> None:
        self.grow()


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    p1 = Plant("rose", 25, 30, 90)
    change = 0.0
    for x in range(1, 8):
        change += p1.grow()
        print(f"=== Day {x} ===")
        p1.show()
        if x % 7 == 0:
            print(f"Growth this week: {change}cm")
            change = 0
    p1.age()
    p2 = Plant("rose", 25, 30, 50)
    p2.grow()
    p3 = Plant("rose", 25, 30, 10)
    p3.grow()
