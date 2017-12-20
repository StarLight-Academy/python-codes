class Student(object):

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        self.avg = self._calc_avg()
        self.grade = self._calc_grade()

    def _calc_avg(self):
        return sum(self.marks) / len(self.marks)

    def _calc_grade(self):
        if self.avg >= 80:
            return 'A'
        elif self.avg >= 65:
            return 'B'
        elif self.avg >= 50:
            return 'C'
        elif self.avg >= 33:
            return 'D'
        else:
            return 'E'

    def print_student(self):
        print()
        print('-'*50)
        print('Name: ' + self.name + '\t\tAge: ' + str(self.age))
        print('Marks' + '-'*45)
        for i in range(1, len(self.marks)+1):
            print(str(i) + '. ' + str(self.marks[i-1]))
        print('Average: ' + str(self.avg) + '\t\tGrade: '+self.grade)


if __name__ == '__main__':
    name = input('Enter Name: ')
    age = int(input('Enter Age: '))
    marks = []
    print('Enter Marks in 5 subjects --- ')
    for i in range(1, 6):
        marks.append(float(input('Marks in subject ' + str(i) + ': ')))
    s = Student(name, age, marks)
    s.print_student()
