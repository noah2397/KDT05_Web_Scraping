'''
– 자신이 가지고 있는 카드 관리
Ø 두 개의 리스트를 가짐 (holding_card_list, open_card_list)
– 두 장의 동일한 카드를 제거하는 기능
Ø 번호가 동일한 경우, holding_card_list에서 open_care_list로 이동: 테이블에 공개하는 기능
'''
from card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.holding_card_list = list()
        self.open_card_list = list()
    def add_card_list(self, card_list):
        pass
    def display_two_card_lists(self):
        # 두 개의 리스트를 출력하는 기능
        # 리스트의 항목들을 하나씩 가져와서 print(card) 형태로 출력
        print("=" * 60) # 줄 출력
        print(f"[{self.name}] : Open card list: {len(self.open_card_list)}\n")
        # for문을 이용하여 하나씩 가져옴
        for i in range(len(self.open_card_list)):
            # 카드 객체를 생성하고
            card=Card(self.open_card_list[i][0], self.open_card_list[i][1])
            # print(Card)를 사용하여 Card.py에 __str__ 메서드를 불러옴
            print(card, end=" ")
        print("\n\n") # 줄 띄어쓰기
        # 아래도 위와 같은 방식으로 출력
        print(f"[{self.name}] : Holding card list: {len(self.holding_card_list)}\n")
        for i in range(len(self.holding_card_list)):
            card = Card(self.holding_card_list[i][0], self.holding_card_list[i][1])
            print(card, end=" ")
        print()

    def check_one_pair_card(self):
        # 번호가 동일한 경우, holding_card_list에서 open_care_list로 이동: 테이블에 공개하는 기능
        print("="*60)
        print(f"[{self.name}: 숫자가 같은 한쌍의 카드 검사]")


        # 알파벳을 숫자로 바꾸는 딕셔너리 생성
        change_dict = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11,
                       "Q": 12, "K": 13}
        duplicate = dict() # 숫자 : 인덱스 를 기억하는 duplicate 딕셔너리 생성
        for i, v in enumerate(self.holding_card_list):
            try:
                duplicate[change_dict[v[1]]]
                # 일단 v[1]<-숫자&알파벳 값을 change_dict안에 넣어 일괄 숫자로 변경,
                # 그러고나서 해당 숫자를 키값으로 가지는 딕셔너리 요소가 있는지 확인
            except KeyError: # 만약 없어서 KeyError가 난다면
                duplicate.setdefault(change_dict[v[1]], []) # 새로 숫자 : 인덱스를 기억하는 딕셔너리 요소 생성
            duplicate[change_dict[v[1]]].append(i) # 값이 있었다면, 원래 있던 값에 새로운 인덱스 정보 추가

        '''
        시간복잡도를 O(n)으로 만들기 위해 해당 방법을 사용함
        duplicate : {7:[1,3], 9:[2], 3:[4,7,9], 10:[5], 11:[6,8]}
        --> 7값을 가진 애가 1,3번째 인덱스에 있고, 3값을 가진 애가 4,7,9에 있음
        --> 11값을 가진 애가 6,8번째 인덱스에 있으므로,
        --> 총 3쌍의 카드를 open_card_list에 보내야한다
        '''
        del_index = [] # holding_card_list에 있는 카드들을 제거하기 위한 리스트 생성
        while True:
            break_key=0 # flag변수 : 숫자가 같은 카드가 2개 발견되지 않으면, 종료함
            for key, value in duplicate.items(): # 숫자:인덱스 요소를 하나씩 꺼내면서 진행
                if len(value) >= 2 : # 만약 숫자가 겹치는 카드가 있다면
                    break_key=1 # 같은 숫자 4개인 카드도 있을 수 있기에, 두 개만 처리하고,
                                # 또 while문을 돌아서 나머지 두 개를 처리해야하기 때문에
                                # break_key를 1로 설정함

                    # open_card_list에 카드들을 추가함
                    self.open_card_list.append(self.holding_card_list[value[0]])
                    self.open_card_list.append(self.holding_card_list[value[1]])
                    # holding_card_list에 카드를 제거하기 위해 인덱스 값을 저장
                    del_index.append(value[0])
                    del_index.append(value[1])
                    # open_card_list에 추가한 카드들은 duplicate딕셔너리에서 삭제
                    value.remove(value[0])
                    value.remove(value[0]) # 앞에걸 지웠으므로, 인덱스 0으로 다시 삭제
            if break_key==0 : break # 탈출 조건

        for i in del_index:
            self.holding_card_list[i] = "" # del_index에 있는 인덱스를 가진 녀석들은 다 공백으로 바꿈
        #공백인 애들을 필터링하여 holding_card_list 갱신
        self.holding_card_list = list(filter(lambda item: item != "", self.holding_card_list))
        self.display_two_card_lists() # 두 명의 카드들을 보여줌

if __name__ == "__main__" :
    test=Player("Tom")