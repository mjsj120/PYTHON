python = "python is Amazing"
print(python.lower())  #소문자
print(python.upper())  #대문자
print(python[0].isupper())  #TRUE
print(len(python))  #파이썬 문자열 길이 #17
print(python.replace("python", "JAVA"))  #JAVA is Amazing

index = python.index("n") #문자의 위치 
print(index)  #5
index = python.index("n", index + 1) #6번째부터 계산
print(index)  #15

print(python.find("n")) #5
print(python.find("JAVA")) # -1 #원하는 값이 없을 때는 -1 반환
# print(python.index("JAVA")) > 오류
print("hi")

print(python.count("n"))  #2
