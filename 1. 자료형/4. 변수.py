#변수 :  값을 저장하는 공간

#애완동물을 소개해주세요.
#우리집강아지의 이름은연탄이예요
#연탄이는4살이며,산책을 아주 좋아해요
#연탄이는 어른일까요?True


animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집" +  animal + "의 이름은" + name +"예요")
print(name + "는" + str(age) + "살이며," + hobby + "을 아주 좋아해요") #str : 정수형을 문자열로 바꿔주는 역할
print(name + "는 어른일까요?" + str(is_adult)) #boolean형도 str사용



#우리집강아지의 이름은연탄이예요
#연탄이 는 4 살이며, 공놀이 을 아주 좋아해요
#연탄이는 어른일까요?True

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집" +  animal + "의 이름은" + name +"예요")
hobby = "공놀이"
print(name, "는" , age, "살이며,", hobby, "을 아주 좋아해요") #',' 사용가능 & 정수형변수, boolean 변수 그대로 사용 가능(str 사용 x), 빈칸 1개 생성됨
print(name + "는 어른일까요?" + str(is_adult)) 
