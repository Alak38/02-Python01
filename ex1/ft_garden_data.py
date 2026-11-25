#!/usr/bin/python3

class Plant:
    def __init__(self, nm: str, hgt: float, ag: int) -> None:
        self.name = nm
        self.height = hgt
        self.age = ag

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}", end="")
        print(f"cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    Plant("rose", 25, 30).show()
    Plant("sunflower", 80, 45).show()
    Plant("cactus", 15, 120).show()
