import random
from time import sleep

ans = ["숙제가 참 쉽죠?! 와~신난다...",
       "누가 챗봇소리를 내었는가",
       "코로나바이러스때문에 재택근무 하고싶어요",
       "그냥 재택근무가 하고 싶은 베짱이"]
finish = ["quit", "exit"]
print("반갑습니다. 최첨단 인공지능 대화로봇을 지향만합니다.")

while True:
    choice = random.randint(0, 3)
    answer = ans[int(choice)]
    a = input("아무거나 물어보세요~\n>")
    a.strip()
    # 'input'에 공백이 들어왔을 때, 제거는?
    if a.strip().lower() in finish:
        break
    elif a.strip() == '':
        print("뭐라도 말을 해야 답인지 알려주지.. 다시해요")
    else:
        print("제 대답은요..", end="")
        sleep(0.3)
        print(".", end="")
        sleep(0.3)
        print(".", end="")
        sleep(0.3)
        print(".", end="")
        print(answer)

input("엔터치면 마칩니다.")



