from .character import Character

class Warrior(Character):
    def __init__(self, name="전사", level=1):
        super().__init__(name, level, health=100, attack_power=15)

    def attack(self, target):
        print(f"{self.name}의 기본 공격!")
        target.take_damage(self.attack_power)

    def special_attack(self, target):
        print(f"{self.name}의 [강력한 일격]!")
        damage = self.attack_power * 2
        target.take_damage(damage)
        self.health -= 5  # 본인 체력 5 감소
        print(f"{self.name}도 반동으로 5의 피해를 입음 (남은 체력: {self.health})")
