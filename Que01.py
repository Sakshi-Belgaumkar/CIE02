import sys

if len (sys.argv) == 5:
    name = sys.argv[1]
    usn = sys.argv[2]
    department = sys.argv[3]
    semester = sys.argv [4]
else:
    name = "Sakshi"
    usn = 155
    department = "BCA"
    semester = "Third"

print("Student profile card")
print("Student name:",name)
print("Student USN",usn)
print("Student Department:",department)
print("Student semester:", semester)
