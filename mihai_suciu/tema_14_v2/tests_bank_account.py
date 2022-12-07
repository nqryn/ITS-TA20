import pytest
from mock import patch
from pct4_bank_account import BankAccount


@pytest.fixture
def dummy_account():
    dummy_account = BankAccount('John Doe', 'GB04 1238 RONC 3123 1234', 0, 0)
    return dummy_account


@patch('builtins.print')
def test_print_account_balance(mock_print, dummy_account):
    dummy_account.print_account_balance()
    mock_print.assert_called_with(f"Holder: {dummy_account.account_holder}\nAccount: {dummy_account.account_code}\nAmount: {dummy_account.account_balance} Euros\nCredit: {dummy_account.account_credit} Euros")

