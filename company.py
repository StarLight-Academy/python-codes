from datetime import datetime
import os


COMPANY_NAME = "\t\t\t   ABC PVT. LTD."
COMPANY_ADD = "\t\t\t B2/23 xyz Colony\n\t\t\t New Delhi - 110003"


class Employee(object):
    def __init__(self, emp_id, name, position, grade_pay, basic_pay, ta_basic, ma):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.grade_pay = grade_pay
        self.basic_pay = basic_pay
        self.ta_basic = ta_basic
        self.ma = ma

    def _calc_epf(self):
        return 0.12 * self.basic_pay

    def _calc_itax(self):
        return 0.2 * self.basic_pay

    def _calc_hra(self):
        return 0.3 * (self.basic_pay + self.grade_pay)

    def _calc_da(self):
        return 1.32 * (self.basic_pay + self.grade_pay)

    def _calc_total(self):
        return (self.basic_pay + self.grade_pay +
                self._calc_hra() + self._calc_da())

    def _calc_ta(self):
        return 1.32 * self.ta_basic

    def _calc_total_pay(self):
        return (self.basic_pay + self.grade_pay +
                self._calc_hra() + self._calc_da() +
                self.ta_basic + self._calc_ta() + self.ma)

    def _calc_deduce(self):
        return self._calc_epf() + self._calc_itax()

    def print_employee(self, now):
        print(COMPANY_NAME)
        print(COMPANY_ADD)
        print("\t\t\t\t\t\t\tDate: " + str(now.day) + '/' + str(now.month) + '/' + str(now.year))
        print("\n\tEmployee Number: " + str(self.emp_id) + '\tName: ' + self.name + '\t\tPost: ' + self.position)
        print("\n\t  Payment\t\t\t\t\t Deduction")
        print("\tBasic Pay: " + str(self.basic_pay) + '\t\t\t\tEPF: ' + str(self._calc_epf()))
        print("\tGrade Pay: " + str(self.grade_pay) + "  \t\t\t\tITAX: " + str(self._calc_itax()))
        print("\tTotal: " + str(self._calc_total()))
        print("\tHRA: " + str(self._calc_hra()))
        print("\tDA: " + str(self._calc_da()))
        print("\tTABASIC: " + str(self.ta_basic))
        print("\tTA: " + str(self._calc_ta()))
        print("\tMA: " + str(self.ma))
        print("\n\tTotal Pay: " + str(self._calc_total_pay()) + "\t\t\t Total Deduction: " + str(self._calc_deduce()))

    def generate_pay_slip(self, now):
        with open(self.name + '.txt', 'w') as f:
            f.write(COMPANY_NAME)
            f.write('\n' + COMPANY_ADD)
            f.write("\n\t\t\t\t\t\t\tDate: " + str(now.day) + '/' + str(now.month) + '/' + str(now.year))
            f.write("\n\n\tEmployee Number: " + str(self.emp_id) + '\tName: ' + self.name + '\t\tPost: ' + self.position)
            f.write("\n\n\t  Payment\t\t\t\t\t Deduction")
            f.write("\n\tBasic Pay: " + str(self.basic_pay) + '\t\t\t\tEPF: ' + str(self._calc_epf()))
            f.write("\n\tGrade Pay: " + str(self.grade_pay) + "  \t\t\t\tITAX: " + str(self._calc_itax()))
            f.write("\n\tTotal: " + str(self._calc_total()))
            f.write("\n\tHRA: " + str(self._calc_hra()))
            f.write("\n\tDA: " + str(self._calc_da()))
            f.write("\n\tTABASIC: " + str(self.ta_basic))
            f.write("\n\tTA: " + str(self._calc_ta()))
            f.write("\n\tMA: " + str(self.ma))
            f.write("\n\n\tTotal Pay: " + str(self._calc_total_pay()) + "\t\t\t Total Deduction: " + str(self._calc_deduce()))

    def generate_pay_slip_and_print(self):
        now = datetime.now()
        self.print_employee(now)
        self.generate_pay_slip(now)


def get_new_id(li):
    if len(li) == 0: return 1
    max_id = li[0].emp_id
    for i in range(1, len(li)):
        if li[i].emp_id > max_id:
            max_id = li[i].emp_id
    return max_id


def enter_new_employee(emp_id):
    name = input('Enter Name: ')
    position = input('Enter Position: ')
    grade_pay = float(input('Enter Grade Pay: '))
    basic_pay = float(input('Enter Basic Pay: '))
    ta_basic = float(input('Enter TABASIC: '))
    ma = float(input('Enter ma: '))
    return Employee(emp_id, name, position, grade_pay,
                    basic_pay, ta_basic, ma)


def find_employee(employees, emp_id):
    for i in range(len(employees)):
        if employees[i].emp_id == emp_id:
            return True, i
    return False, None



if __name__ == '__main__':
    employees = []
    while True:
        print('\t\tMENU')
        print('-' * 50)
        print('\t1. Enter New Employee Details')
        print('\t2. Make Employee Pay Slip')
        print('\t3. Delete Employee')
        print('\t4. Update Employee')
        print('\t5. Display Employee')
        print('\t6. Exit')
        print('-' * 50)
        choice = int(input('Enter Your Choice: '))
        if choice == 1:
            employees.append(enter_new_employee(get_new_id(employees)))
            print('\nID Given: '+str(employees[-1].emp_id))
        elif choice == 2:
            emp_id = int(input('Enter Employee ID: '))
            is_found, emp_pos = find_employee(employees, emp_id)
            if is_found:
                employees[emp_pos].generate_pay_slip(datetime.now())
                print("Generate Pay Slip")
            else:
                print("Employee Doesn't exist.")
        elif choice == 3:
            emp_id = int(input('Enter Employee ID: '))
            is_found, pos = find_employee(employees, emp_id)
            if is_found:
                del employees[pos]
            else:
                print("Employee Doesn't exist.")
        elif choice == 4:
            emp_id = int(input('Enter Employee ID: '))
            is_found, emp_pos = find_employee(employees, emp_id)
            if is_found:
                employees[emp_pos] = enter_new_employee(employees[emp_pos].emp_id)
            else:
                print("Employee Doesn't exist.")
        elif choice == 5:
            emp_id = int(input('Enter Employee ID: '))
            is_found, emp_pos = find_employee(employees, emp_id)
            if is_found:
                employees[emp_pos].print_employee()
            else:
                print("Employee Doesn't exist.")
        else:
            print('Program Terminating!!!')
            break
