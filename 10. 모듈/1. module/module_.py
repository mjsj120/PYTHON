import module
module.price(3) #3명이서 영화 보러 갔을 때 가격
module.price_morning(4) #4명이서 조조 할인 영화 보러 갔을 때
module.price_soldier(5) #5명의 군인이 영화 보러 갔을 때
# 3명 가격은 300000원입니다.
# 4명 조조 할인 가격은 24000원입니다.
# 5명 군인 할인 가격은 20000원입니다.

import module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)
# 3명 가격은 300000원입니다.
# 4명 조조 할인 가격은 24000원입니다.
# 5명 군인 할인 가격은 20000원입니다.

from module import *
#from random import *
price(3)
price_morning(4)
price_soldier(5)
# 3명 가격은 300000원입니다.
# 4명 조조 할인 가격은 24000원입니다.
# 5명 군인 할인 가격은 20000원입니다.

from module import price, price_morning
price(5)
price_morning(6)
# 5명 가격은 500000원입니다.
# 6명 조조 할인 가격은 36000원입니다.
#price_soldier(7)  #오류

from module import price_soldier as price
price(5)
# 5명 군인 할인 가격은 20000원입니다.