#!/usr/bin/python3

class Plant:
    def __init__(self: Plant, nm: str, hgt: float, ag: int, hlth: int) -> None:
        self.name = nm
        self.height = hgt
        self.days = ag
        self.health = hlth

    def show(self: Plant) -> Plant:
        print(f"{self.name.capitalize()}: {self.height}", end="")
        print(f"cm, {self.days} days old")
        return (self)

    def grow(self: Plant) -> Plant:
        self.show()
        growrate = 0.975 + (self.health * 0.0005)
        if self.health * 2 < self.days:
            growrate = 0.95
        elif self.health < self.days:
            growrate = 0.975
        base = self.height
        for x in range(1, 8):
            print(f"=== Day {x} ===")
            self.height = round(self.height * growrate, 1)
            self.days += 1
            self.show()
        else:
            base = round(self.height - base, 1)
            print(f"Growth this week: {base}cm")
        return (self)

    def age(self: Plant) -> Plant:
        self.grow()
        return (self)


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    rose = Plant("rose", 25.0, 30, 30).show()
    print("Created: ", end="")
    Plant("oak", 200.0, 365, 70).show()
    print("Created: ", end="")
    Plant("cactus", 5.0, 90, 100).show()
    print("Created: ", end="")
    Plant("sunflower", 80.0, 45, 80).show()
    print("Created: ", end="")
    Plant("fern", 15.0, 120, 70).show()
