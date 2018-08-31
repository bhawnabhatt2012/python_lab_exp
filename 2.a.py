def bubble(list):
    for i in range(0, len(list) - 1):
        for j in range(1, len(list) - i):
            if (list[j - 1] > list[j]):
                temp = list[j - 1]
                list[j - 1] = list[j]
                list[j] = temp



akshay = {"himanshi": 3, "tejasvini": 5, "nainy": 2, "akshita": 1, "harshit": 2, "ashish": 3, "vishaka": 2, "bhawna": 3,"tekur":2}
himanshi = {"nainy": 3, "bhawna": 5, "akshay": 2, "vishaka": 1, "tekur": 2, "harshit": 3, "ashish": 2, "akshita": 5,"tejasvini": 5}
tejasvini= {"harshit": 3, "bhawna": 5, "ashish": 2, "vishaka": 1, "akshay": 2, "tekur": 3, "nainy": 2, "akshita": 5,"himanshi": 5}
bhawna = {"nainy": 3, "himanshi": 5, "harshit": 2, "vishaka": 1, "akshay": 2, "ashish": 3, "tekur": 2, "tejasvini": 5,"akshita": 5}
akshita = {"akshay": 3, "bhawna": 5, "ashish": 2, "tekur": 1, "vishaka": 2, "nainy": 3, "harshit": 2, "tejasvini": 5,"himanshi": 5}
nainy = {"himanshi": 3, "harshit": 5, "akshita": 2, "tekur": 1, "akshay": 2, "tejasvini": 3, "ashish": 2, "vishaka": 5,"bhawna": 5}
vishaka= {"bhawna": 3, "nainy": 5, "tekur": 2, "akshay": 1, "himanshi": 2, "tejasvini": 3, "ashish": 2, "harshit": 5,"akshita": 5}
harshit = {"himanshi": 3, "akshay": 5, "tejasvini": 2, "bhawna": 1, "akshita": 2, "nainy": 3, "vishaka": 2, "ashish": 5,"tekur": 5}
ashish = {"tekur": 3, "harshit": 5, "vishaka": 2, "akshay": 1, "nainy": 2, "akshita": 3, "tejasvini": 2, "bhawna": 5,"himanshi": 5}
tekur= {"bhawna": 3, "himanshi": 5, "vishaka": 2, "akshita": 1, "ashish": 2, "akshita": 3, "utejasvini": 2, "harshit": 5,"nainy": 5}




akshayvalue=himanshi["akshay"]+tejasvini["akshay"]+nainy["akshay"]+akshita["akshay"]+harshit["akshay"]+ashish["akshay"]+vishaka["akshay"]+bhawna["akshay"]+tekur["akshay"];
himanshivalue=nainy["himanshi"]+bhawna["himanshi"]+akshay["himanshi"]+vishaka["himanshi"]+tekur["himanshi"]+harshit["himashi"]+ashish["himanshi"]+akshita["himanshi"]+tejasvini["himanshi"];
tejasvinivalue=harshit["tejasvini"]+bhawna["tejasvini"]+ashish["tejasvini"]+vishaka["tejasvini"]+akshay["tejasvini"]+tekur["tejasvini"]+nainy["tejasvini"]+akshita["tejasvini"]+himanshi["tejasvini"];
bhawnavalue=tejasvini["bhawna"]+himanshi["bhawna"]+akshita["bhawna"]+akshay["bhawna"]+vishaka["bhawna"]+nainy["bhawna"]+harshit["bhawna"]+tekur["bhawna"]+ashish["bhawna"];
akshitavalue=himanshi["akshita"]+tejasvini["akshita"]+bhawna["akshita"]+akshay["akshita"]+vishaka["akshita"]+nainy["akshita"]+harshit["akshita"]+tekur["akshita"]+ashish["akshita"];
# final_list=[tarunvalue,adityavalue,gauravvalue,arghyavalue,prateekvalue];
# print(final_list);
# bubble(final_list);
# print("most popular friend is",final_list[4]);
final={"akshay":akshayvalue,"himanshi":himanshivalue,"tejasvini":tejasvinivalue,"bhawna":bhawnavalue,"akshita":akshitavalue};
final1=sorted(final, key=final.get);
print(final);
highest=final1[len(final1)-1];
print("most popular friend is",highest);





