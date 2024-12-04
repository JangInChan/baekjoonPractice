def get_grade(score):
    if score >= 4.0:
        return 'A'
    if score >= 3.0:
        return 'B'
    if score >= 2.0:
        return 'C'
    if score >= 1.0:
        return 'D'
    else:
        return 'F'

score = float(input("Enter your score: "))

grade = get_grade(score)

print(grade)