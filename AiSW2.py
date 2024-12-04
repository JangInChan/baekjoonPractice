# 분을 시간과 분으로 변환하는 함수
def convert_minutes(total_minutes):
    hours = total_minutes // 60  # 시간은 분을 60으로 나눈 몫
    minutes = total_minutes % 60  # 남은 분은 나머지
    return hours, minutes

# 사용자로부터 분 입력 받기
total_minutes = int(input("분 입력: "))

# 변환된 시간과 분 계산
hours, minutes = convert_minutes(total_minutes)

# 결과 출력
print(f"결과값: {hours}시간 {minutes}분")