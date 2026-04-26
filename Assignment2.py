print('''-------------------| Assignment-2 | QUESTIONS & ANSWERS |----------------------------''')
print()
print("Question-1")
print('''Your school has following grading based upon the marks (M) obtained by a student :
      o if M<10, the grade will be E.
      o if >11M<20, the grade will be D.
      o if >21M<30, the grade will be C.
      o if >31M<40, the grade will be B.
      o if >41M<50, the grade will be A.
      Your friend will enter his marks out of 5050, and your task is to print his grades using
      a switch statement.
      Note : You have to complete findGrade function. No need to take any input.''')

m = 19

if(m >= 41 and m <= 50):
    print("Grade A")
elif(m >= 31 and m <= 40):
    print("Grade B")
elif(m >= 21 and m <= 30):
    print("Grade C")
elif(m >= 11 and m <= 20):
    print("Grade D")
else:
    print("Grade E")

print("----------------------------------------------------------------------------------------")

print("Question-2 - Pending")
print('''You are provided with a table containing some characters and their corresponding values.
      Your task will be to find the value from the table corresponding to an input character and 
      return it.
      
      |P or p - PrepBytes |
      |Z or z - Zenith |
      |E or e - Expert Coder |
      |D or d - Data Structure |

      Note : You have to complete getValue function. No need to take any input.''')


def find_value(ch):
    if ch == 'P' and ch == 'p':
        return "PrepBytes"
    elif ch == 'Z' and ch == 'z':
        return "Zenith"
    elif ch == 'E' and ch == 'e':
        return "Expert Code"
    elif ch == 'D' and ch == 'd':
        return "Data Structure"

print(find_value('p'))
print(find_value('P'))
print(find_value('d'))
print(find_value('E'))

print("----------------------------------------------------------------------------------------")

print("Question-3")
print('''Take three numbers and print the largest number among them if all of three are same print -1-1.
      Note : You have to complete Max_out_of_three. No need to take any input.''')
      
A3 = 2
B3 = 5
C3 = 4

def Max_out_of_three(A3,B3,C3):
    if A3 == B3 and B3 == C3:
        return -1
    else :
        print(max(A3,B3,C3))

Max_out_of_three(A3,B3,C3)

print("----------------------------------------------------------------------------------------")

print("Question-4 Pending")
print('''You are given 33 distinct integers X, Y and Z your task is to find and return the 
      second smallest integer among the three provided integers.
      Note : You have to complete findSndSmallest function. No need to take any input.''')

x4 = 2
y4 = 9
z4 = 23

def findSndSmallest(x4,y4,z4):
    nums = [x4,y4,z4]
    nums.sort()
    return nums[1]

print(findSndSmallest(x4,y4,z4))

print("----------------------------------------------------------------------------------------")

print("Question-5")
print('''Write a program takes three angles and checks whther the tringle is acute or obtuse.
      Note : You have to complete Triangle_Check. No need to take any input.''')



A5 = 60
B5 = 100
C5 = 20

def Triangle_Check(A5, B5, C5):
    if A5<90 and B5<90 and C5<90:
        return "Accute"
    elif A5>90 or B5>90 or C5>90:
        return "Obtuse"

print(Triangle_Check(A5, B5, C5))

