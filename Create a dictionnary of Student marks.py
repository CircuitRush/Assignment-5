students = {
    "Het": 85,
    "Priya": 92,
    "Amit": 78,
    "Neha": 88
}

name = input("Enter Student's name : ")

if name in students:
    print(f"Student's marks are : {students[name]}")
else:
    print("Student not found.")