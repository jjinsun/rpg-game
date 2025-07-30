from .character import Character
import random

class Rogue(Character):
    def __init__(self, name="도적", level=1):
        super().__init__(name, level, health=90, attack_power=12)

    def attack(self, target):
        print(f"{self.name}의 기본 공격!")
        target.take_damage(self.attack_power)

    def special_attack(self, target):
        print(f"{self.name}의 급습⚔️!")
        if random.random() < 0.7:
            damage = self.attack_power * 3
            print("급습 성공!")
            target.take_damage(damage)
        else:
            print("급습 실패!")
