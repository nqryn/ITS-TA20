import pytest
from mock import patch
from pct3_employee import Employee


@pytest.fixture()
def employee_test():
    employee_4_test = Employee('Doe', 'John', 1000)
    return employee_4_test


@patch('builtins.print')
def test_employee_description(mock_print, employee_test):
    employee_test.employee_description()
    mock_print.assert_called_with(f"Employee: {employee_test.last_name} "
                                  f"{employee_test.first_name} Salary:"
                                  f" {employee_test.salary}")


@patch('builtins.print')
def test_employee_full_name(mock_print, employee_test):
    employee_test.employee_full_name()
    mock_print.assert_called_with(f"Full name: {employee_test.last_name} {employee_test.first_name}")


@patch('builtins.print')
def test_employee_monthly_salary(mock_print, employee_test):
    employee_test.employee_monthly_salary()
    mock_print.assert_called_with(f"Monthly salary: {employee_test.salary}")


@patch('builtins.print')
def test_employee_yearly_salary(mock_print, employee_test):
    employee_test.employee_yearly_salary()
    mock_print.assert_called_with(f"Yearly salary: {employee_test.salary * 12}")


@patch('builtins.print')
def test_employee_salary_raise(mock_print, employee_test):
    employee_test.employee_salary_raise(10)
    mock_print.assert_called_with(f"{employee_test.last_name} {employee_test.first_name} has a salary raise of 10%")


@pytest.fixture()
def employee_test2():
    employee_4_test2 = Employee('Doe', 'John', 1000)
    employee_4_test2.employee_salary_raise(10)
    return employee_4_test2


@patch('builtins.print')
def test_employee_salary_raise(mock_print, employee_test2):
    employee_test2.employee_monthly_salary()
    mock_print.assert_called_with(f"Monthly salary: {employee_test2.salary}")