"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0 or score > 100:    # or function for 100
    print("Invalid score")
#elif score > 100:
   # print("Invalid score")
elif score >= 90:
    print("excellent")
elif score >= 50:
    print("pass")
else:
    print("bad")
