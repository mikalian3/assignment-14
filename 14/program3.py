class Student:
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.enrolled_credits = enrolled_credits
    def compute_tuition(self):
        rates = {"I": 250.00, "O": 500.00, "X": 800.00, "G": 250.00}
        tuition = self.enrolled_credits * rates[self.district_code]
        return tuition
student1 = Student("Mike", "Luchanok", "I", 12)
student2 = Student("Mark", "Smith", "O", 16)
student3 = Student("Ilia", "Kun", "X", 12)
student4 = Student("Beka", "Tut", "G", 15)
print(f"{student1.first_name} {student1.last_name}")
print(f"District code: {student1.district_code}")
print(f"Enrolled credits: {student1.enrolled_credits}")
print(f"Tuition owed: {student1.compute_tuition():.2f}")
print()
print(f"{student2.first_name} {student2.last_name}")
print(f"District code: {student2.district_code}")
print(f"Enrolled credits: {student2.enrolled_credits}")
print(f"Tuition owed: {student2.compute_tuition():.2f}")
print()
print(f"{student3.first_name} {student3.last_name}")
print(f"District code: {student3.district_code}")
print(f"Enrolled credits: {student3.enrolled_credits}")
print(f"Tuition owed: {student3.compute_tuition():.2f}")
print()
print(f"{student4.first_name} {student4.last_name}")
print(f"District code: {student4.district_code}")
print(f"Enrolled credits: {student4.enrolled_credits}")
print(f"Tuition owed: {student4.compute_tuition():.2f}")