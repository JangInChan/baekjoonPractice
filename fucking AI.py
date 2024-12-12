#8-5
"""def sum_even_odd():
  even = 0
  odd = 0
  for n in range(1, 101):
    if n % 2 == 0:
      even = even + n
    else:
      odd = odd + n
  return even, odd

e, o = sum_even_odd()
print("1-100까지 짝수 합: ", e)
print("1-100까지 홀수 합: ", o) """

#8-11
""" def oper(x, y):
  oplist = []
  op1 = x + y
  op2 = x - y
  oplist.append(op1)
  oplist.append(op2)
  return oplist

num1 = int(input("첫 번째 수: "))
num2 = int(input("두 번째 수: "))
reslist = oper(num1, num2)
print("두 수합: %d" % reslist[0])
print("두 수차: %d" % reslist[1]) """

#8-13
""" def grade(score):
  if score >= 90.0:
    return 'A'
  elif score >= 80.0:
    return 'B'
  elif score >= 70.0:
    return 'C'
  elif score >= 60.0:
    return 'D'
  else:
    return 'F'
  
score = int(input("점수 입력: "))
print("학점은 %c 입니다." % grade(score)) """

#8-14
""" def avg(score):
  t = 0
  for i in score:
    t = t + i
  return t/len(score)

def pass_fail(score):
  if avg(score) >= 60:
    return 'PASS'
  else:
    return 'FAIL'
  
def max(score):
  max = 0
  for i in score:
    if i > max:
      max = i
  return max

score = [80, 90, 40, 70, 60]
print("평균 점수: %.1f" % avg(score))
print("최대 점수: %d" % max(score))
print("합격 여부: %s" % pass_fail(score)) """

#10-5
""" import turtle as t

n = int(t.textinput("도형채우기", '''*********************************************
1. 삼각형 2. 사각형 3. 원
                    *********************************************'''))
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
t.end_fill() """