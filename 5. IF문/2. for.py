# 대기번호 : 0
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4

for waiting_no in range(5): #0, 1, 2, 3, 4
    print("대기번호 : {0}".format(waiting_no))
    

# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4
# 대기번호 : 5
for waiting_no in range(1,6): # 1, 2, 3, 4, 5
    print("대기번호 : {0}".format(waiting_no))
    
#아이언맨, 커피가 준비되었습니다
#토르, 커피가 준비되었습니다
#아이엠 그루트, 커피가 준비되었습니다
starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다".format(customer))  