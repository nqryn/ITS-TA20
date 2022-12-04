from pct3_employee import Employee


def test_employee_description():
    employee_test = Employee('John', 'Doe', 1000)
    assert employee_test.last_name == 'John' and \
           employee_test.first_name == 'Doe' and \
           employee_test.salary == 1000


def test_employee_full_name():
    employee_test = Employee('John', 'Doe', 1000)
    assert employee_test.employee_full_name() == 'John Doe'


def test_employee_monthly_salary():
    employee_test = Employee('John', 'Doe', 1000)
    assert employee_test.employee_monthly_salary() == 1000


def test_employee_yearly_salary():
    employee_test = Employee('John', 'Doe', 1000)
    assert employee_test.employee_yearly_salary() == 12000


def test_employee_salary_raise():
    employee_test = Employee('John', 'Doe', 1000)
    employee_test.employee_salary_raise(10)
    assert employee_test.salary == 1100
