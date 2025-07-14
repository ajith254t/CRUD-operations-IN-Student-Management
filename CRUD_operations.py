import json

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

class StudentManager:
    def __init__(self):
        self.students = []
        self.load_data()
    
    def load_data(self):
        try:
            with open("students.json", "r") as file:
                self.students = json.load(file)
        except FileNotFoundError:
            self.students = []
    
    def save_data(self):
        with open("students.json", "w") as file:
            json.dump(self.students, file, indent=4)
    
    def add_student(self, name, age, grade):
        new_student = Student(name, age, grade)
        self.students.append(new_student.to_dict())
        self.save_data()
        print(f"Student {name} added successfully!")
    
    def view_students(self):
        if not self.students:
            print("No students found.")
            return
        for idx, student in enumerate(self.students, start=1):
            print(f"{idx}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    
    def update_student(self, index, name, age, grade):
        if index < 0 or index >= len(self.students):
            print("Invalid student index!")
            return
        self.students[index] = Student(name, age, grade).to_dict()
        self.save_data()
        print(f"Student {name} updated successfully!")
    
    def delete_student(self, index):
        if index < 0 or index >= len(self.students):
            print("Invalid student index!")
            return
        del self.students[index]
        self.save_data()
        print("Student deleted successfully!")

def main():
    manager = StudentManager()
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            manager.add_student(name, age, grade)
        elif choice == '2':
            manager.view_students()
        elif choice == '3':
            index = int(input("Enter student index to update: ")) - 1
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            grade = input("Enter new grade: ")
            manager.update_student(index, name, age, grade)
        elif choice == '4':
            index = int(input("Enter student index to delete: ")) - 1
            manager.delete_student(index)
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
