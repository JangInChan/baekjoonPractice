import turtle
import random

# 스크린 설정
screen = turtle.Screen()
screen.bgcolor("#2b2d42")
screen.title("Turtle Graphics Assignment")

# 터틀 설정
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# 색상 팔레트
colors = ["#ff6b6b", "#feca57", "#48dbfb", "#1dd1a1", "#5f27cd", "#341f97", "#ee5253", "#0abde3"]

# 꽃잎 그리기 함수
def draw_petals(radius, angle, count):

    for _ in range(count):
        t.color(colors[_ % len(colors)])  # 색상 순환
        t.begin_fill()
        for _ in range(2):  # 두 개의 곡선을 합쳐 하나의 꽃잎 생성
            t.circle(radius, angle)
            t.left(180 - angle)
        t.end_fill()
        t.left(360 / count)

# 꽃잎을 여러 레이어로 구성
def draw_flower_layers():

    for i in range(5):
        t.penup()
        t.goto(0, 0)  # 중심 기준으로 이동
        t.setheading(0)
        t.pendown()
        draw_petals(radius=50 + 15 * i, angle=60, count=12 + i * 2)

# 꽃 중앙의 포인트 추가
def draw_center():

    t.penup()
    t.goto(0, -40)  # 중심부를 정확히 꽃 중앙으로 이동
    t.setheading(0)
    t.pendown()
    t.color("#ffd700")  # 금빛 중앙
    t.begin_fill()
    t.circle(40)
    t.end_fill()

# 꽃 중앙 장식 추가
def draw_center_decoration():

    t.penup()
    t.goto(0, 0)
    t.pendown()
    for i in range(12):
        t.color(random.choice(colors))
        t.penup()
        t.goto(0, 0)
        t.setheading(i * 30)  # 방사형으로 위치 이동
        t.forward(60)
        t.pendown()
        t.begin_fill()
        t.circle(8)  # 작은 원으로 장식
        t.end_fill()

# 배경의 별 추가
def draw_stars(count):
    t.penup()
    for _ in range(count):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        t.goto(x, y)
        t.dot(random.randint(3, 6), "#ffffff")  # 작은 흰색 점을 별처럼 표현
    t.pendown()

# 메인 실행
turtle.colormode(255)

# 화려한 꽃 그리기
draw_flower_layers()
draw_center()
draw_center_decoration()

# 배경 장식
draw_stars(100)

# 텍스트 메시지 추가
t.penup()
t.goto(0, -250)  # 화면 하단 중앙에 배치
t.color("white")
t.write("과제 제출", align="center", font=("Arial", 18, "bold"))

# 터틀 화면 유지
screen.mainloop()
