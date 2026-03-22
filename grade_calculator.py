def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A", "Excellent! Keep shining 🌟"
    elif 80 <= marks < 90:
        return "B", "Very Good! Keep it up 👍"
    elif 70 <= marks < 80:
        return "C", "Good! You can do even better 💪"
    elif 60 <= marks < 70:
        return "D", "Needs improvement, don’t give up!"
    elif 0 <= marks < 60:
        return "F", "Work harder, success will come!"
    else:
        return None, "Invalid marks"

while True:
    name = input("Enter student name: ")
    try:
        marks = int(input("Enter marks (0-100): "))
        grade, message = calculate_grade(marks)
        if grade:
            print(f"\n📊 RESULT FOR {name.upper()}:")
            print(f"Marks: {marks}/100")
            print(f"Grade: {grade}")
            print(f"Message: {message}")
            break
        else:
            print("❌ Marks must be between 0 and 100. Try again.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")