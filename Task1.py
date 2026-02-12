'''Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.'''

students = {
    "Alice": 85,
    "Vaishnavi": 90,
    "Avantika": 92,
    "Madhura": 88
}

student_name = input("Enter the student's name: ")

if student_name in students:
    print(f"{student_name}'s marks: {students[student_name]}")

else:
    print(f"'{student_name}' record not found.")
    

