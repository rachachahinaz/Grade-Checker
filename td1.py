
print("hello sir , We will calculate the result for you")
score=int(input("enter the student's grade :" ))
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

grade = calculate_grade(score)
print("The grade is:", grade)