# Name: Ida Bagus Ryogassa Avatara (Ryo)
# Teacher: Mr Jude
# Class: Intro to Programming L1AC

class1 = int(input('Number of Students for Class 1: '))
class2 = int(input('Number of Students for Class 2: '))
class3 = int(input('Number of Students for Class 3: '))
print()
group1 = int(input('Number of Groups for Class 1: '))
group2 = int(input('Number of Groups for Class 2: '))
group3 = int(input('Number of Groups for Class 3: '))

# Divmod (Quotient and remainder)
studentNum1, leftover1 = divmod(class1, group1)
studentNum2, leftover2 = divmod(class2, group2)
studentNum3, leftover3 = divmod(class3, group3)

print("Number of students in each group")
print("Class 1: ", studentNum1)
print("Class 2: ", studentNum2)
print("Class 3: ", studentNum3)
print()
print("Number of students leftover")
print("Class 1: ", leftover1)
print("Class 2: ", leftover2)
print("Class 3: ", leftover3)





