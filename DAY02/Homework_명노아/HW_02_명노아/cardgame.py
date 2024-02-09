#– 각 클래스의 객체 생성 및 게임 진행



from card import Card
from player import Player
from gamedealer import GameDealer
def play_game():
    # 1단계==================================================
    # 두 명의 player 객체 생성
    player1 = Player("흥부") # 흥부 Player 객체 생성
    player2 = Player("놀부") # 놀부 Player 객체 생성
    dealer = GameDealer() # GameDealer 객체 생성
    dealer.make_deck() # 52개의 카드 생성
    print(dealer) # GameDealer가 가지고 있는 카드 목록(deck)을 화면에 출력
    dealer.shuffle() # 52개의 카드 섞기

    dealer.divide_init(player1, player2) # 10장씩 나눠주기
    player1.display_two_card_lists() # 흥부의 카드 보여주기
    player2.display_two_card_lists() # 놀부의 카드 보여주기
    # =======================================================
    # 2단계===================================================
    print("\n[2]단계 : 다음 단계 진행을 위해 Enter 키를 누르세요!",'😊😊😊😊'*2)
    input()
    print(dealer)
    player1.check_one_pair_card()
    player2.check_one_pair_card()
    # =======================================================
    # 3~6단계===================================================
    for i in range(3,7):
        print(f"\n[{i}]단계 : 다음 단계 진행을 위해 Enter 키를 누르세요!",'😊😊😊😊'*2)
        input()
        dealer.divide(player1, player2)
        print(dealer)
        player1.check_one_pair_card()
        player2.check_one_pair_card()
        if len(dealer.deck) == 0 or len(player1.holding_card_list) == 0 or len(player2.holding_card_list) == 0:
            print("게임종료!")
            break
    # =======================================================

if __name__ == '__main__':
    play_game()