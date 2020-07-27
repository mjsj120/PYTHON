# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) #{'커피', '주스', '우유'} <class 'set'> #자료형태 set

menu = list(menu)
print(menu, type(menu))  #['주스', '우유', '커피'] <class 'list'> #자료형태 list

menu = tuple(menu)
print(menu, type(menu)) #('주스', '우유', '커피') <class 'tuple'> #자료형태 tuple

menu = set(menu)
print(menu, type(menu))  #{'커피', '우유', '주스'} <class 'set'> #자료형태 set