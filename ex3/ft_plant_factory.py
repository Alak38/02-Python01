#!/usr/bin/python3

class Plant:
    def __init__(self, nm: str, hgt: float, ag: int, hlth: int) -> None:
        self.name = nm
        self.height = round(hgt, 1)
        self.days = ag
        self.health = hlth

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}", end="")
        print(f"cm, {self.days} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    rose = Plant("rose", 25.0, 30, 30)
    rose.show()
    print("Created: ", end="")
    oak = Plant("oak", 200.0, 365, 70)
    oak.show()
    print("Created: ", end="")
    cact = Plant("cactus", 5.0, 90, 100)
    cact.show()
    print("Created: ", end="")
    sunf = Plant("sunflower", 80.0, 45, 80)
    sunf.show()
    print("Created: ", end="")
    fern = Plant("fern", 15.0, 120, 70)
    fern.show()
