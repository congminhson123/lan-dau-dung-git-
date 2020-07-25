class Employee:
    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last
        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def _raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Son', 'Cong Minh', 50000)
print(emp_1.pay)
Employee._raise(emp_1)
print(emp_1.pay)
print(Employee.num_of_emp)
name = "bim"
s1 = input()
s2 = input()

tmp = s1[0:2]
s1 = s2[0:2] + s1[2:]
s2 = tmp + s2[2:]

print(s1 + " " + s2)
