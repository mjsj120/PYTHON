#sep 
print("python", "java", sep=",")
# python,java
print("python", "java", sep=" vs ")
# python vs java

#end
print("python", "java", sep=",")
print("무엇이 더 재밌을까요?")
# python,java
# 무엇이 더 재밌을까요?

print("python", "java", sep=",", end = "?")
print("무엇이 더 재밌을까요?")
# python,java?무엇이 더 재밌을까요?

import sys
print("python", "java", file = sys.stdout) #stdout : 표준 출력
print("python", "java", file = sys.stderr) #stderr : 표준 에러

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():  #items : key, value를 쌍으로 tuple로 보내줌
    print(subject, score)    
# 수학 0
# 영어 50
# 코딩 100

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():  #items : key, value를 쌍으로 tuple로 보내줌
    print(subject.ljust(8), str(score).rjust(4), sep=":") #ljust : 왼쪽 정렬, ljust(8): 8칸 확보
                                                 #rjust : 오른쪽 정렬
# 수학      :   0
# 영어      :  50
# 코딩      : 100


#은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 :" + str(num).zfill(3)) #zfill : 빈공간 0, zfill(3) : 3공간 확보, 빈공간은 0
# 대기번호 :001
# 대기번호 :002
# 대기번호 :003
# 대기번호 :004
# 대기번호 :005
# 대기번호 :006
# 대기번호 :007
# 대기번호 :008
# 대기번호 :009
# 대기번호 :010
# 대기번호 :011
# 대기번호 :012
# 대기번호 :013
# 대기번호 :014
# 대기번호 :015
# 대기번호 :016
# 대기번호 :017
# 대기번호 :018
# 대기번호 :019
# 대기번호 :020


answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) #사용자 코드로 입력시 항상 문자열
# <class 'str'>
# 입력하신 값은 안뇽입니다.

answer = 10
print(type(answer))
# <class 'int'>