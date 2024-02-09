'''
– 1벌의 카드(deck) 생성 기능: 리스트로 구현
– 각 Player들에게 카드를 나누어 주는 기능
Ø 자신이 가진 deck에서 제거하여 다른 선수들에게 제공
'''

from card import Card
import random
from player import Player
class GameDealer:
    def __init__(self): # 카드셋 초기화
        self.deck = list()
        self.suit_number = 13
    def make_deck(self): # 카드 생성
        print("[GameDealer] 초기 카드 생성")
        print("-"*30)
        card_suits = ["♠", "♥", "♣", "◆"]
        card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        card_deck=[]
        for shape in card_suits : # 형태 반복
            for num in card_numbers : # 숫자 반복 (2중 for문 사용)
                card_deck.append((shape, num)) # card_deck에 하나하나씩 넣음
        self.deck = card_deck # 만들어진 덱을 인스턴스 변수로 저장

    def __str__(self): # 딜러 카드 출력
        print(f"[GameDealer] 딜러가 가진 카드 수 : {len(self.deck)}")
        for i,v in enumerate(self.deck, start=1) :
            print(v, end=" ")
            if i % 13 == 0: # 13개마다 한 줄씩 띄어쓰기
                print()
        return "" # 오류 방지
    def shuffle(self): # 카드를 섞는 함수
        random.shuffle(self.deck)
    def divide_init(self, player1, player2):
        '''
        각 Player에게 초기 10장씩 나누어 줌
        deck[]에서 10장씩 각 Player에게 줌
        deck[]에서는 총 20장의 카드가 삭제됨
        :param player1:
        :param player2:
        :return:
        '''
        player1.holding_card_list = self.deck[:10]
        del self.deck[:10]
        player2.holding_card_list = self.deck[:10]
        del self.deck[:10]
    def divide(self, player1, player2):
        # 각 Player에게 4장씩 카드를 나누어 줌
        player1.holding_card_list.extend(self.deck[:4])
        del self.deck[:4]
        player2.holding_card_list.extend(self.deck[:4])
        del self.deck[:4]




if __name__ == "__main__" :
    test=GameDealer()
    test.make_deck()
    print(test.deck)
    print(test)
    test.shuffle()
    print(test)