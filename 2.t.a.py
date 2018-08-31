from collections import Counter

akshay = {"himanshi": 2, "tejasvini": 5, "nainy": 2, "akshita": 1, "harshit": 2, "ashish": 3, "vishaka": 2, "bhawna": 3,"tekur":2}
himanshi = {"nainy": 3, "bhawna": 5, "akshay": 2, "vishaka": 1, "tekur": 2, "harshit": 3, "ashish": 2, "akshita": 5,"tejasvini": 5}
tejasvini= {"harshit": 3, "bhawna": 5, "ashish": 2, "vishaka": 1, "akshay": 2, "tekur": 3, "nainy": 2, "akshita": 5,"himanshi": 5}
bhawna = {"nainy": 3, "himanshi": 5, "harshit": 2, "vishaka": 1, "akshay": 2, "ashish": 3, "tekur": 2, "tejasvini": 5,"akshita": 5}
akshita = {"akshay": 3, "bhawna": 5, "ashish": 2, "tekur": 1, "vishaka": 2, "nainy": 3, "harshit": 2, "tejasvini": 5,"himanshi": 5}
nainy = {"himanshi": 3, "harshit": 5, "akshita": 2, "tekur": 1, "akshay": 2, "tejasvini": 3, "ashish": 2, "vishaka": 5,"bhawna": 5}
vishaka= {"bhawna": 3, "nainy": 5, "tekur": 2, "akshay": 1, "himanshi": 2, "tejasvini": 3, "ashish": 2, "harshit": 5,"akshita": 5}
harshit = {"himanshi": 3, "akshay": 5, "tejasvini": 2, "bhawna": 1, "akshita": 2, "nainy": 3, "vishaka": 2, "ashish": 5,"tekur": 5}
ashish = {"tekur": 3, "harshit": 5, "vishaka": 2, "akshay": 1, "nainy": 2, "akshita": 3, "tejasvini": 2, "bhawna": 5,"himanshi": 5}
tekur= {"bhawna": 3, "himanshi": 5, "vishaka": 2, "akshita": 1, "ashish": 2, "akshita": 3, "utejasvini": 2, "harshit": 5,"nainy": 5}

first=Counter(himanshi)
second=Counter(bhawna)
third= Counter(tejasvini)
fourth=Counter(akshita)
fifth=Counter(akshay)
sixth=Counter(nainy)
seventh=Counter(harshit)
eighth=Counter(vishaka)
ninth=Counter(tekur)
tenth=Counter(ashish)


total_value=first+second+third+fourth+fifth+sixth+seventh+eighth+ninth+tenth
total_score=dict(total_value)
print("MOST POPULAR FRIEND WITH HIGHEST RATING:",str(max(total_score.items(),key=lambda k:k[1])))
