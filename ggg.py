def convert_minutes(total_minutes):
    h = total_minutes // 60
    m = total_minutes % 60
    return h, m

total_minutes = int(input("분 입력: "))

h, m = convert_minutes(total_minutes)

print(f"결과값: {h}시간 {m}분")