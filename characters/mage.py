from .character import Character

class Mage(Character):
    def __init__(self, name="마법사", level=1):
        super().__init__(name, level, health=80, attack_power=18)
        self.mana = 100

    def attack(self, target):
        print(f"{self.name}의 기본 공격!")
        target.take_damage(self.attack_power)

    def special_attack(self, target):
        if self.mana < 20:
            print(f"{self.name}의 마나가 부족합니다! (남은 마나: {self.mana})")
            raise Exception("마나 부족")
        print(f"{self.name}의 [파이어볼]!")
        damage = int(self.attack_power * 1.5)
        target.take_damage(damage)
        self.mana -= 20
        print(f"{self.name}의 마나가 20 감소 (남은 마나: {self.mana})")
