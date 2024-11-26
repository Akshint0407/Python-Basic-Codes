# Program to find intersections, differences, unions, and specific group memberships of students playing different sports.

# Input: Students playing cricket
a = int(input("Enter the number of students playing cricket: "))
crick = []
for i in range(a):
    a1 = input(f"Enter the name of student {i + 1} playing cricket: ")
    crick.append(a1)

# Input: Students playing badminton
b = int(input("Enter the number of students playing badminton: "))
bad = []
for i in range(b):
    b1 = input(f"Enter the name of student {i + 1} playing badminton: ")
    bad.append(b1)

# Input: Students playing football
c = int(input("Enter the number of students playing football: "))
foot = []
for i in range(c):
    c1 = input(f"Enter the name of student {i + 1} playing football: ")
    foot.append(c1)

# Function to find intersection (common students between two lists)
def inter(lst1, lst2):
    res1 = []
    for i in lst1:
        if i in lst2:  # Check if a student is in both lists
            res1.append(i)
    print("\nStudents playing both cricket and badminton:", res1)
    return res1

# Function to find the difference (students in lst1 but not in lst2)
def diff(lst1, lst2):
    res2 = []
    for i in lst1:
        if i not in lst2:  # Check if a student is in lst1 but not in lst2
            res2.append(i)
    print("\nStudents playing cricket but not badminton:", res2)
    return res2

# Function to find the union (all unique students from two lists)
def union(lst1, lst2):
    res3 = lst1.copy()  # Start with all students in lst1
    for i in lst2:
        if i not in lst1:  # Add only those students not already in lst1
            res3.append(i)
    print("\nUnion of students playing cricket and badminton:", res3)
    return res3

# Function to find students playing only cricket and football but not badminton
def block(lst1, lst2, lst3):
    res4 = []
    for i in lst1:
        if i in lst3 and i not in lst2:  # Check if a student is in cricket and football but not badminton
            res4.append(i)
    print("\nStudents playing only cricket and football but not badminton:", res4)
    return res4

# Call the functions and display results
inter(crick, bad)
diff(crick, bad)
union(crick, bad)
block(crick, bad, foot)
