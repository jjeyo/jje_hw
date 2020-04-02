from tkinter import *

#### 변수설정:
canvas_height = 400
canvas_width = 600
canvas_colour = "black"

p1_x = canvas_width / 2
p1_y = canvas_height
p1_colour = "green"
line_width = 10
line_length = 100

need_dot = False


# 함수:
def put_dot(p1_x, p1_y, width):
    canvas.create_oval(x - width / 2, y - width / 2, x + width / 2, y + width / 2, fill=p1_colour, width = 0)


def p1_move_n(event):
    global p1_y, need_dot

    canvas.create_line(p1_x, p1_y, p1_x, (p1_y - line_length), width=line_width, fill=p1_colour)
    if need_dot:
        put_dot(p1_x, p1_y, line_width)
    p1_y = p1_y - line_length
    need_dot = True


def p1_move_s(event):
    global p1_y, need_dot

    canvas.create_line(p1_x, p1_y, p1_x, (p1_y + line_length), width=line_width, fill=p1_colour)
    if need_dot:
        put_dot(p1_x, p1_y, line_width)
    p1_y = p1_y + line_length
    need_dot = True


def p1_move_e(event):
    global p1_x, need_dot

    canvas.create_line(p1_x, p1_y, (p1_x + line_length), p1_y, width=line_width, fill=p1_colour)
    if need_dot:
        put_dot(p1_x, p1_y, line_width)
    p1_x = p1_x + line_length
    need_dot = True


def p1_move_w(event):
    global p1_x, need_dot

    canvas.create_line(p1_x, p1_y, p1_x - line_length, p1_y, width=line_width, fill=p1_colour)
    if need_dot:
        put_dot(p1_x, p1_y, line_width)
    p1_x = p1_x - line_length
    need_dot = True


def erase_all(event):
    global need_dot
    canvas.delete(ALL)
    need_dot = False


# 메인:
window = Tk()
window.title("MyEtchASketch")
canvas = Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()

# 키를 눌렀을 때 움직임
window.bind("<Up>", p1_move_n)
window.bind("<Down>", p1_move_s)
window.bind("<Right>", p1_move_e)
window.bind("<Left>", p1_move_w)
window.bind("e", erase_all)

window.mainloop()
