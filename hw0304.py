import random


def comparing_function(number_1, number_2):
    if number_1 > number_2:
        return 0
    elif number_1 < number_2:
        return 1


pick_num = random.randint(100, 999)
count = 1

while True:
    try:
        user_num = int(input('숫자맞추기 게임입니다. 100 부터 999 사이의 3자리 숫자를 입력해주세요.\n>'))
        if 100 < (user_num % 1000) < 1000:
            break
        elif (user_num % 1000) < 100:
            print('100에서 999사이의 3자리 숫자를 입력해주세요.\n')
    except ValueError:
        print('문자가 아닌 숫자만 입력해주세요.\n')
        continue

while True:
    if pick_num == user_num:
        break
    result = comparing_function(pick_num, user_num)
    if result == 0:
        print("Up")
    elif result == 1:
        print("Down")
    count = count + 1
    user_num = int(input('다시 숫자를 맞춰보세요.\n>'))

if count > 10:
    print("%s 이상 시도했어요. 잘 못맞추시네요. 추측 잘 못하는 스타일이신가봐요." % count)
elif 3 < count <= 10:
    print("%s 회 도전해서 맞췄어요. 아쉽지만, 맞추는 일은 내 맘 같지 않죠.." % count)
elif 1 < count <= 3:
    print("%s 회 도전해서 맞췄어요. 감각있는 스타일! 잘 맞추시는 편이에요." % count)
elif count == 1:
    print("로또를 구입해야하는 날인가봐요. 한번에 맞췄어요.")


