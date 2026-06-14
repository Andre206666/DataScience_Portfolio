import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grades(self, subject, grade):
        self.grades[subject] = grade

    def get_average(self):
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        return f"Name: {self.name}, Grades: {self.grades}"

student = Student("Andre")
student.add_grades("Math", 90)
student.add_grades("Science", 85)
student.add_grades("English", 92)
print(student)
print(f"Average: {student.get_average():.1f}")

class GradeAnalyzer:
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)

    def get_top_student(self):
        return sorted(self.students, key=lambda s: s.get_average(), reverse=True)[0]

    def get_class_average(self):
        return sum(s.get_average() for s in self.students) / len(self.students)

    def to_data_frame(self):
        data = []
        for s in self.students:
            data.append({"name": s.name, **s.grades})
        return pd.DataFrame(data)

student_analyzer = GradeAnalyzer()
student_analyzer.add_student(student)
student_analyzer.to_data_frame()
print(student_analyzer.to_data_frame())

s1 = Student("Andre")
s1.add_grades("Math", 90)
s1.add_grades("Science", 85)

s2 = Student("Maria")
s2.add_grades("Math", 95)
s2.add_grades("Science", 88)

s3 = Student("John")
s3.add_grades("Math", 75)
s3.add_grades("Science", 80)

analyzer = GradeAnalyzer()
analyzer.add_student(s1)
analyzer.add_student(s2)
analyzer.add_student(s3)

print(f"Top student: {analyzer.get_top_student().name}")
print(f"Class average: {analyzer.get_class_average():.1f}")
print(analyzer.to_data_frame())

class GradeReport:
    def __init__(self,analyzer):
        self.analyzer = analyzer

    def plot_averages(self):
        df = self.analyzer.to_data_frame()
        df.set_index('name')['Math'].plot(kind='bar')
        plt.title("Math Grades")
        plt.xlabel("Grade")
        plt.ylabel("Math")
        plt.show()

    def plot_subject_comparison(self):
        df = self.analyzer.to_data_frame()
        df.set_index('name').plot(kind='bar')
        plt.title('Subject Comparison')
        plt.xlabel('Student')
        plt.ylabel('Grade')
        plt.show()

    def summary(self):
        print(f"Top student: {self.analyzer.get_top_student().name}")
        print(f"Class average: {self.analyzer.get_class_average():.1f}")

report = GradeReport(analyzer)
report.summary()
report.plot_averages()
report.plot_subject_comparison()

conn = sqlite3.connect("grades.db")
c = conn.cursor()
c.execute("""
      CREATE TABLE IF NOT EXISTS grades (
      id INTEGER PRIMARY KEY,
      students_name TEXT,
      subject TEXT,
      grade REAL)
""")
conn.commit()
print("Database created!")

def save_grade(students_name, subject, grade):
    c.execute("""
    INSERT INTO grades (students_name, subject, grade) VALUES (?, ?, ?)""",
              (students_name, subject, grade))
    conn.commit()

for s in [s1, s2, s3]:
    for subject, grade in s.grades.items():
        save_grade(s.name, subject,grade )

c.execute("SELECT * FROM grades")
print(c.fetchall())