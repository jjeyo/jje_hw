import random


pick_num = random.randint(100, 999)
count_s = 0
count_b = 0

while True:
    while True:
        try:
            user_num = int(input('야구게임입니다. 100 부터 999 사이의 3자리 숫자를 입력해주세요.\n>'))
            if 100 < (user_num % 1000) < 1000:
                break
            elif (user_num % 1000) < 100:
                print('100에서 999사이의 3자리 숫자를 입력해주세요.\n')
        except ValueError:
            print('문자가 아닌 숫자만 입력해주세요.\n')
            continue

    nl_1 = str(pick_num)
    nl_2 = str(user_num)
    for i in range(0, 3):
        if nl_2[i] == nl_1[i]:
            count_s = count_s + 1
        elif nl_2.find(nl_1[i]) != -1:
            count_b = count_b + 1
        else:
            continue
    if count_s == 3:
        break
    else:
        print("%s, %s strike, %s ball" % (pick_num, count_s, count_b))
        count_s = 0
        count_b = 0

print('Home Run!')
