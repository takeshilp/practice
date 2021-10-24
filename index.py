class Student:

    def __init__(self, name, birth_date, address):
        self.name = name
        self.birth_date = birth_date
        self.address = address



class Group:

    def __init__(self, name):
        self.name = name
        self.students = []

    def add(self, student):
        self.students.append(student)


    def remove(self, student):
        if student in self.students:
            self.students.remove(student)


    def show(self):
        print(self.students)

student_1 = Student('Мулярчук Илья Владимирович', '19.12.2003', 'г.Курган, центр')
student_2 = Student('Хертек Илья  Олегович', '14.09.1997', 'г.Курган, центр')
group_1 = Group('ИТ-33')
group_1.add(student_1)
group_1.add(student_2)

group_1.show()
group_1.remove(student_2)
group_1.show()

for el in group_1.students:
    print(el.birth_date)

del group_1

print(student_1)