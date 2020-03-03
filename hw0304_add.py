import random

# player1이 중복되지 않은 1~9까지의 숫자를 3개 고르기
pick_num = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]
while len(set(pick_num)) != 3:
    pick_num = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]

# player2의 입력값을 받아서 검토하기
while True:
    while True:
        try:
            user_num = int(input('야구게임입니다. 0을 제외한 3자리 숫자를 입력해주세요.\n>'))
            if 100 < (user_num % 1000) < 1000:
                user_num = list(str(user_num))
                if user_num[1] != '0' and user_num[2] != '0':
                    break
        except ValueError:
            continue

# player2의 올바른 입력값을 player1의 랜덤 숫자와 비교하여 야구게임하기
    count_s = 0
    count_b = 0

    for i in range(0, 3):
        for k in range(0, 3):
            if i == k and str(pick_num[i]) == user_num[k]:
                count_s = count_s + 1
            elif i != k and str(pick_num[i]) == user_num[k]:
                count_b = count_b + 1
    if count_s == 3:
        break
    print("%s strike, %s ball" % (count_s, count_b))

print('Home Run!')



