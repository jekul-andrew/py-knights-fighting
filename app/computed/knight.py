class Knight:

    def __init__(self, knight: dict) -> None:
        self.name = knight.get("name")
        self.power = knight.get("power")
        self.hp = knight.get("hp")
        self.armour = knight.get("armour", [])
        self.weapon = knight.get("weapon")
        self.potion = knight.get("potion")
        self.protection = 0

        # ---------- Recalculate
        self.recalculate_stats()

    def recalculate_stats(self) -> None:

        # Armour
        for protection in self.armour:
            self.protection += protection.get("protection", 0)

        # Power
        self.power += self.weapon.get("power", 0)

        if self.potion is not None:

            effect = self.potion.get("effect", {})

            if "power" in effect:
                self.power += effect.get("power", 0)

            if "protection" in effect:
                self.protection += effect.get("protection", 0)

            if "hp" in effect:
                self.hp += effect.get("hp", 0)
