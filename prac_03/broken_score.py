"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    result = university_grade(score)
    print(result)


def university_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "pass"
    else:
        return "bad"


main()