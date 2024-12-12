import turtle as t

n = int(t.textinput("도형채우기", '''******************************
1.삼각형 2.사각형 3.원
******************************'''))
t.fillcolor(0.8, 0, 0.8)
t.begin_fill()
if n == 1:
    for x in range(3):
        t.forward(100)
        t.left(120)
elif n == 2:
    for x in range(4):
        t.forward(100)
        t.left(90)
elif n == 3:
    t.circle(50)
else:
    t.write("잘못 입력하셨습니다!", font = ("맑은 고딕", 18, "bold"))
t.end_fill()