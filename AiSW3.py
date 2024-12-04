# 점수에 따른 학점을 반환하는 함수
def get_grade(score):
    if score >= 4.0:
        return "A"
    elif score >= 3.0:
        return "B"
    elif score >= 2.0:
        return "C"
    elif score >= 1.0:
        return "D"
    else:
        return "F"

# 사용자로부터 점수 입력 받기
score = float(input("점수 입력: "))

# 학점 계산
grade = get_grade(score)

# 결과 출력
print(f"학점은 {grade}입니다.")
