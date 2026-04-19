'''
Q1.Find Grades Your school has the following grading system based upon the marks (M) obtained by
a student:  

If M≤10, the grade will be E. 
If 11≥M≤20, the grade will be D. 
If 21≥M≤30, the grade will be C. 
If 31≥M≤40, the grade will be B. 
If 41≥M≤50, the grade will be A. 

Your friend will enter his marks out of 5050, and your task is to print his grades using a switch 
statement. Note: You have to complete findGrades function. No need to take any input.

'''

M = int(input("Enter your marks : "))

if (M >= 40) and (M <= 50):
    print("Grade A")

elif (M >= 30) and (M <= 40):
    print("Grade B")

elif (M >= 20) and (M <= 30):
    print("Grade C")

elif (M >= 11) and (M <= 20):
    print("Grade D")

else :
    print("Invalid entry")