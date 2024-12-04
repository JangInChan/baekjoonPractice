# 섭씨 온도를 화씨 온도로 변환하는 함수
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# 화씨 온도를 섭씨 온도로 변환하는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# 사용자에게 입력을 받아서 선택하게 함
choice = int(input("섭씨 온도 입력 1번, 화씨 온도 입력 2번 선택: "))

# 사용자가 1번(섭씨 온도 입력)을 선택한 경우
if choice == 1:
    celsius = float(input("섭씨온도 입력: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"변환된 화씨 온도: {fahrenheit:.2f}")

# 사용자가 2번(화씨 온도 입력)을 선택한 경우
elif choice == 2:
    fahrenheit = float(input("화씨온도 입력: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"변환된 섭씨 온도: {celsius:.2f}")

# 잘못된 선택을 한 경우
else:
    print("잘못된 선택입니다. 1 또는 2를 입력하세요.")
