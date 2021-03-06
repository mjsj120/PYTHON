# Quiz) 당신은 cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객

from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1~ 50이라는 수(승객)
    time =  randrange(5, 51) # 5분 ~50분 소요시간
    if 5 <= time <=15: # 5분 ~15분 이내의 손님, 탑승 승객 수 증가 처리
        print("[0] {0}번째 손님 (소요시간 : {1}분".format(i, time))
        cnt += 1
    else: #매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i, time))
print("총 탑승 승객 : {0}분".format(cnt))

# [0] 1번째 손님 (소요시간 : 13분
# [ ] 2번째 손님 (소요시간 : 32분
# [0] 3번째 손님 (소요시간 : 10분
# [ ] 4번째 손님 (소요시간 : 36분
# [ ] 5번째 손님 (소요시간 : 29분
# [ ] 6번째 손님 (소요시간 : 16분
# [0] 7번째 손님 (소요시간 : 6분 
# [ ] 8번째 손님 (소요시간 : 49분
# [ ] 9번째 손님 (소요시간 : 18분
# [ ] 10번째 손님 (소요시간 : 17분
# [0] 11번째 손님 (소요시간 : 13분
# [ ] 12번째 손님 (소요시간 : 34분
# [ ] 13번째 손님 (소요시간 : 37분
# [ ] 14번째 손님 (소요시간 : 28분
# [ ] 15번째 손님 (소요시간 : 50분
# [ ] 16번째 손님 (소요시간 : 44분
# [ ] 17번째 손님 (소요시간 : 23분
# [ ] 18번째 손님 (소요시간 : 24분
# [ ] 19번째 손님 (소요시간 : 22분
# [0] 20번째 손님 (소요시간 : 15분
# [ ] 21번째 손님 (소요시간 : 22분
# [0] 22번째 손님 (소요시간 : 15분
# [ ] 23번째 손님 (소요시간 : 21분
# [ ] 24번째 손님 (소요시간 : 47분
# [ ] 25번째 손님 (소요시간 : 24분
# [0] 26번째 손님 (소요시간 : 5분
# [ ] 27번째 손님 (소요시간 : 18분
# [ ] 28번째 손님 (소요시간 : 28분
# [ ] 29번째 손님 (소요시간 : 50분
# [ ] 30번째 손님 (소요시간 : 22분
# [ ] 31번째 손님 (소요시간 : 21분
# [ ] 32번째 손님 (소요시간 : 34분
# [ ] 33번째 손님 (소요시간 : 26분
# [ ] 34번째 손님 (소요시간 : 47분
# [ ] 35번째 손님 (소요시간 : 40분
# [ ] 36번째 손님 (소요시간 : 28분
# [ ] 37번째 손님 (소요시간 : 50분
# [ ] 38번째 손님 (소요시간 : 43분
# [ ] 39번째 손님 (소요시간 : 43분
# [ ] 40번째 손님 (소요시간 : 39분
# [ ] 41번째 손님 (소요시간 : 26분
# [0] 42번째 손님 (소요시간 : 9분
# [ ] 43번째 손님 (소요시간 : 31분
# [ ] 44번째 손님 (소요시간 : 43분
# [ ] 45번째 손님 (소요시간 : 46분
# [0] 46번째 손님 (소요시간 : 14분
# [ ] 47번째 손님 (소요시간 : 18분
# [ ] 48번째 손님 (소요시간 : 35분
# [ ] 49번째 손님 (소요시간 : 33분
# [ ] 50번째 손님 (소요시간 : 41분
# 총 탑승 승객 : 9분