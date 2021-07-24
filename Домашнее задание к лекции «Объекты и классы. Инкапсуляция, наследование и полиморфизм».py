class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avr = 0

    def rate_for_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avr_rate(self):
        l = []
        for value in self.grades.values():
            for each in value:
                l.append(each)
        self.avr = sum(l) / len(l)

    def __str__(self):
        pr = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avr}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return pr


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        pr = f'Имя: {self.name}\nФамилия: {self.surname}'
        return pr


class Lecturer(Mentor):
    def __init__(self, name, surname, ):
        super().__init__(name, surname)
        self.grades = {}
        self.avr = 0

    def avr_rate(self):
        l = []
        for value in self.grades.values():
            for each in value:
                l.append(each)
        self.avr = sum(l) / len(l)

    def __str__(self):
        pr = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avr}'
        return pr


def avr_for_students(students, course):
    l = []
    for student in students:
        for each in student.grades[course]:
          l.append(each)
    general_avr = sum(l) / len(l)
    print(f'Средняя оценка студентов по курсу {course} равняется: {general_avr}')

def avr_for_lecturers(lecturers, course):
    l = []
    for lecturer in lecturers:
        for each in lecturer.grades[course]:
            l.append(each)
    general_avr = sum(l) / len(l)
    print(f'Средняя оценка лекторов по курсу {course} равняется: {general_avr}')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Java']
bad_student = Student('Ken', 'boy', 'men')
bad_student.courses_in_progress += ['Python']


best_lecturer = Lecturer('имя', 'фамилия')
best_lecturer.courses_attached += ['Python', 'Git']
bad_lecturer = Lecturer('name', 'surname')
bad_lecturer.courses_attached += ['Python']
print(best_lecturer.courses_attached)
best_student.rate_for_lecturer(best_lecturer, 'Python', 10)
best_student.rate_for_lecturer(bad_lecturer, 'Python', 6)
best_student.rate_for_lecturer(best_lecturer, 'Git', 10)
print(best_lecturer.grades)

reviewer = Reviewer('Roy', 'Keen')
reviewer.courses_attached += ['Python']
reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(bad_student, 'Python', 6)

print(reviewer)

best_lecturer.avr_rate()
print(best_lecturer)

print(best_student)

avr_for_students([best_student, bad_student], 'Python')
avr_for_lecturers([best_lecturer, bad_lecturer],'Python')




