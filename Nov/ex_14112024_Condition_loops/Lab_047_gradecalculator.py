#Grade Calculator
#criteria
# A- 90-100
# B- 80-89
# C- 70-79
# D- 60-69
# E- 0-59

#LOGIC BUILDING FORMULA
# USER INPUT -- SCORE WILL INT
#O/P -- STR (A,B,C,D,E)

score= int(input("Enter score=\n"))

if score>100 and score<=-1:
    print("You are a SUPERMAN")
elif score>=90 and score<=100:
    print("Your grade is A")
elif score>=80 and score<=89:
    print("Your grade is B")
elif score>=70 and score<=79:
    print("Your grade is C")
elif score>=60 and score<=69:
    print("Your grade is D")
else:
    print("Your grade is E")