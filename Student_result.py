

def student_result():
    name = input("Enter student name: ")

    marks = []
    for i in range(1, 6):
        mark = int(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 35:
        grade = "D"
    else:
        grade = "Fail"

    print("\n--- Student Result ---")
    print("Name:", name)
    print("Total Marks:", total, "/ 500")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)


student_result()
