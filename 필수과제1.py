from random import *
number = randint(1,10)
print("1과 10 사이의 숫자를 하나 정했습니다. 이 숫자는 무엇일까요?")
while True:
    user_input = int(input("숫자를 입력하세요:"))
    if number > user_input:
        print("너무 작습니다. 다시 입력하세요.")
    elif number < user_input:
        print("너무 큽니다. 다시 입력하세요.")
    else:
        print("정답입니다.")
        break