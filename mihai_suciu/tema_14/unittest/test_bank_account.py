from pct4_bank_account import BankAccount


def test_print_account_balance():
    account_test = BankAccount('John Doe', 'GB04 1238 RONC 3123 1234', 1000, 0)
    assert account_test.account_holder == 'John Doe' and \
           account_test.account_code == 'GB04 1238 RONC 3123 1234' and \
           account_test.account_balance == 1000 and \
           account_test.account_credit == 0
