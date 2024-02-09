import pandas as pd


storeDF=pd.read_csv("./hollys_branches.csv")
storeDF["위치(시,구)"] = storeDF["위치(시,구)"].str[0:5]
while(True):
    local=input("검색할 매장의 도시를 입력하세요 : ")
    if local.lower()=='quit' : 
        print("종료 합니다.")
        break
    result = storeDF[storeDF["위치(시,구)"]==local].reset_index(drop=True)
    print(f'{"="*20}\n 검색된 매장 수 : {len(result)} \n{"="*20}')
    for i in range(len(result)) :
        print(f"[{i+1:>3}] : {list(result.loc[i,['주소','전화번호']])}")
    print("="*80)