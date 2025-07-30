from characters import Warrior, Mage, Rogue
from battle.battle_manager import BattleManager

def choose_character(prompt):
    while True:
        print(f"\n{prompt}")
        print("1.전사  2.마법사  3.도적")
        choice = input("번호를 입력하세요: ")
        if choice == "1":
            return Warrior()
        elif choice == "2":
            return Mage()
        elif choice == "3":
            return Rogue()
        else:
            print("잘못 입력하셨습니다. 다시 번호만 입력하세요.")

def main():
    print("===== RPG 게임에 오신 걸 환영합니다!🕹️ =====")
    player = choose_character("자신의 캐릭터를 선택하세요.")
    while True:
        enemy = choose_character("상대 캐릭터를 선택하세요.")
        enemy.reset_health()
        player.reset_health()
        bm = BattleManager()
        result = bm.start_battle(player, enemy)
        if not result:
            break
        again = input("계속해서 새로운 적과 싸우시겠습니까? (y/n): ")
        if again.lower() != "y":
            print("게임을 종료합니다.")
            break

if __name__ == "__main__":
    main()
