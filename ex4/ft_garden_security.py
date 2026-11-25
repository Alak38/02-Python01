#!/usr/bin/python3

class Plant:
    def __init__(self, nm: str, hgt: float, ag: int, hlth: int) -> None:
        self.__name = nm
        self.__height = hgt
        self.__days = ag
        self.health = hlth

    def show(self) -> None:
        print(f"{self.__name.capitalize()}: {self.__height}", end="")
        print(f"cm, {self.__days} days old")

    def get_height(self) -> float:
        return (self.__height)

    def get_age(self) -> int:
        return (self.__days)

    def set_height(self, new_h: float) -> None:
        if new_h < 0:
            print("Error, height can't be negative\nHeight update rejected")
        else:
            self.__height = round(new_h, 1)
            print(f"Height updated: {self.__height}")

    def set_age(self, new_d: int) -> None:
        if new_d < 0:
            print("Error, age can't be negative\nAge update rejected")
        else:
            self.__days = round(new_d, 1)
            print(f"Age updated: {self.__days}")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    print("Created: ", end="")
    p1 = Plant("rose", 15.0, 10, 30)
    p1.show()
    p1.set_height(25.0)
    p1.set_age(30)
    print("")
    p1.set_height(-10.0)
    p1.set_age(-30)
    print("\nCurrent status: ", end="")
    p1.show()
