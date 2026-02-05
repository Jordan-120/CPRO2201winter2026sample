import random
from dataclasses import dataclass

@dataclass
class Die:
    __value: int = 1

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value < 1 or value > 6:
            raise ValueError("Die value must be from 1 to 6.")
        self.__value = value


# --- main program ---
die = Die()

random_number = random.randint(1, 10)
print(f"Generated number: {random_number}")

try:
    die.value = random_number
    print(f"{die.value} is accepted")
except ValueError as e:
    print(f"{e} Rejected")
