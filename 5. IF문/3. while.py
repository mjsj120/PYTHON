# while
customer = "토르"
index = 5
while index >=1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -=1 #호출
    if index ==0:
        print("커피는 폐기처분되었습니다.")

# 토르, 커피가 준비 되었습니다. 5번 남았어요.
# 토르, 커피가 준비 되었습니다. 4번 남았어요.
# 토르, 커피가 준비 되었습니다. 3번 남았어요.
# 토르, 커피가 준비 되었습니다. 2번 남았어요.
# 토르, 커피가 준비 되었습니다. 1번 남았어요.
# 커피는 폐기처분되었습니다.
# 토르, 커피가 준비되었습니다.
        
        
customer = "아이언맨"
while True: 
    print("{0}, 커피가 준비되었습니다.호출 {1}회".format(customer, index))
    index +=1
#무한루프
    
    
customer = "토르"
person = "unknown"

while person != customer: #토르가 나올 때까지 무한 루프
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")


# 이름이 어떻게 되세요?아이언맨
# 토르, 커피가 준비되었습니다.
# 이름이 어떻게 되세요?토르