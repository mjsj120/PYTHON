cabinet = {3:"유재석", 100: "김태호"} #key = 3, value = 유재석 
print(cabinet[3]) #유재석
print(cabinet[100]) #김태호
print(cabinet.get(3)) #유재석

# print(cabinet[5]) #프로그램 종료
print(cabinet.get(5)) #None
print(cabinet.get(5, "사용가능")) #None
                                  #사용가능
                                  
print(3 in cabinet) #3이 cabinet에 존재하는지 #TRUE 
print(5 in cabinet) #FALSE

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"]) #유재석
print(cabinet["B-100"]) #김태호

#새 손님
print(cabinet) #{'A-3': '유재석', 'B-100': '김태호'}
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"  #{'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet) #{'B-100': '김태호', 'C-20': '조세호'}

#key들만 출력
print(cabinet.keys()) #dict_keys(['B-100', 'C-20'])

#value들만 출력
print(cabinet.values()) #dict_values(['김태호', '조세호'])

#key, value 쌍으로 출력
print(cabinet.items()) #dict_items([('B-100', '김태호'), ('C-20', '조세호')])

#목욕탕 폐점
cabinet.clear()
print(cabinet)

 