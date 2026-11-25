#!/usr/bin/python3
# from __future__ import annotations

class Plant:
    def __init__(self, nm: str, hgt: float, ag: int, hlth: int) -> None:
        self.name = nm
        self.height = hgt
        self.days = ag
        self.health = hlth

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}", end="")
        print(f"cm, {self.days} days old")

    def grow(self) -> float:
        growrate = 0.975 + (self.health * 0.0005)
        if self.health * 2 < self.days:
            growrate = 0.95
        elif self.health < self.days:
            growrate = 0.975
        base = self.height
        self.height = round(self.height * growrate, 1)
        self.days += 1
        return (round(self.height - base, 1))

    def age(self) -> None:
        self.grow()


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    for x in range(3):
        curr = Plant("rose", 25, 30, (100 - (30 * x + 10)))
        curr.show()
        change = 0.0
        for y in range(1, 8):
            change += curr.grow()
            print(f"=== Day {y} ===")
            curr.show()
            if y % 7 == 0:
                print(f"Growth this week: {change}cm")
                change = 0
