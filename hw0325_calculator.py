memory_set3 = []
memory_number1 = 0
memory_fcn = 0
number1 = 0
number2 = 0
fcn1 = 0
fcn2 = 0
number_temp = []
temp1 = []
temp2 = []
temp = 0
result = 0
set_fcn = ('+', '-', '*', '/', 'c', 'ac')
set_fcn2 = ('%', '+/-')
set_fcn3 = ('mc', 'm+', 'm-')


def add(a, b):   # 더하기 함수
    global number1
    number1 = a + b


def subst(a, b):    # 기 함수
    global number1
    number1 = a - b


def multi(a, b):   # 곱기 함수
    global number1
    number1 = a * b


def division(a, b):   # 나눗셈 함수
    global number1
    number1 = a / b


def integer(a):    # +/- 함수
    global number1
    number1 = a*(-1)


def percentage(a):    # % 함수
    global number1
    number1 = a*(1/100)


def clear():
    global number2, number1
    number2 = 0


def all_clear():
    global number2, number1, fcn2, fcn1
    number1 = 0
    number2 = 0
    fcn1 = 0
    fcn2 = 0


def mp(a):   # m+ 함수
    global memory_set3
    if a >= 0:
        memory_set3.append(a)
    else:
        a = a*(-1)
        memory_set3.append(a)


def mm(a):    # m- 함수
    global memory_set3
    if a <= 0:
        memory_set3.append(a)
    else:
        a = a*(-1)
        memory_set3.append(a)


def mr():    # mr 함수
    global memory_set3
    memory_int_set3 = map(float, memory_set3)
    print(sum(memory_int_set3))


def mc():    # mc 함수
    global memory_set3
    memory_set3 = []


def run_fcn():
    if fcn1 == '+':
        add(number1, number2)
    elif fcn1 == '-':
        subst(number1, number2)
    elif fcn1 == '*':
        multi(number1, number2)
    elif fcn1 == '/':
        division(number1, number2)
    elif fcn1 == '+/-':
        integer(number1)
    elif fcn1 == '%':
        percentage(number1)
    elif fcn1 == 'c':
        clear()
    elif fcn1 == 'ac':
        all_clear()


def run_memory_fcn():
    if memory_fcn == 'm+':
        mp(memory_number1)
    elif memory_fcn == 'm-':
        mm(memory_number1)
    elif memory_fcn == 'mr':
        mr()
    elif memory_fcn == 'mc':
        mc()


def calc():
    global number1, number2, fcn1, temp1, temp2, fcn2, temp, number_temp, set_fcn, memory_set3, memory_number1, memory_fcn
    while True:
        temp = input('>').strip()
        if temp == 'off':
            break
        elif temp in set_fcn:
            if fcn1 != 0:
                fcn1 = temp
                number1 = number2
                number2 = 0
            elif fcn1 == 0:
                fcn1 = temp
        elif temp in set_fcn2:
            fcn1 = temp
            run_fcn()
            print(number1)
        elif temp in set_fcn3:
            memory_fcn = temp
            if fcn1 != 0 and number2 != 0:
                memory_number1 = number2
                run_memory_fcn()
            elif fcn1 == 0 and number1 != 0:
                memory_number1 = number1
                run_memory_fcn()
        elif temp == 'mr':
            mr()
        elif temp == '=':
            if fcn1 != 0:
                run_fcn()
                print(number1)
            elif number1 != 0:
                print(number1)
            else:
                print(number2)
        elif temp == "":
            continue
        else:
            if fcn1 != 0:
                number2 = float(temp)
            else:
                number1 = float(temp)


if __name__ == "__main__":
    calc()


