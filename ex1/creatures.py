from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return "Sproutling heals for a huge amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._transformed:
            return f"{self.name} uses Powered Strike!"
        return f"{self.name} uses Strike!"

    def transform(self):
        self._transformed = True
        return "Shiftling transform"

    def revert(self) -> str:
        self._transformed = False
        return "Shiftling reverts"


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._transformed:
            return f"{self.name} uses Powered Body Slam!"
        return f"{self.name} uses Body Slam!"

    def transform(self):
        self._transformed = True
        return "Morphagon transform"

    def revert(self) -> str:
        self._transformed = False
        return "Morphagon reverts"
