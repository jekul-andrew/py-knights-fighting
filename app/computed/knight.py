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
        self.recalculate_hp()

    def recalculate_hp(self) -> None:

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


if __name__ == "__main__":
    from app.config.config import knights

    # data = knights["lancelot"]
    # lancelot = Knight(data)
    # print(lancelot.__dict__)
    # lancelot.recalculate_hp()
    # print(lancelot.__dict__)
    #
    # print("--------------")
    #
    # data = knights["arthur"]
    # lancelot = Knight(data)
    # print(lancelot.__dict__)
    # lancelot.recalculate_hp()
    # print(lancelot.__dict__)

    # print("--------------")
    #
    # data = knights["mordred"]
    # lancelot = Knight(data)
    # print(lancelot.__dict__)
    # lancelot.recalculate_hp()
    # print(lancelot.__dict__)

    print("--------------")

    data = knights["red_knight"]
    lancelot = Knight(data)
    print(lancelot.__dict__)
    lancelot.recalculate_hp()
    print(lancelot.__dict__)
