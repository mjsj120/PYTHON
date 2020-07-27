#import는 module이나 package만 가능
import package.thailand
trip_to = package.thailand.ThailandPackage()
trip_to.detail()
# [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원

from package.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()
# [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원

from package import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()
# [베트남 패키지 3박 5일] 다낭 효도 여행 60만원

from package import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from package import *
trip_to = thailand.ThailandPackage()
trip_to.detail()