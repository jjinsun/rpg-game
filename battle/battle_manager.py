import random
import time

class BattleManager:
    def start_battle(self, player, enemy):
        print(f"\n--- {player.get_name()} vs {enemy.get_name()} 전투 시작! ---")
        participants = [player, enemy]
        attacker_idx = random.randint(0, 1)
        defender_idx = 1 - attacker_idx

        while player.is_alive() and enemy.is_alive():
            attacker = participants[attacker_idx]
            defender = participants[defender_idx]

            # 공격 방식 선택
            if random.random() < 0.7:
                try:
                    attacker.attack(defender)
                except Exception as e:
                    print(e)
            else:
                try:
                    attacker.special_attack(defender)
                except Exception as e:
                    print(f"특수 공격 실패: {e}")

            defender.show_status()
            time.sleep(1)  # 전투의 딜레이 연출

            # 교대
            attacker_idx, defender_idx = defender_idx, attacker_idx

        if player.is_alive():
            print("\n승리!")
            return True
        else:
            print("\n패배! 게임 종료")
            return False
