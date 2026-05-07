def atm_withdrawal(withdrawal_amount):
    print("Welcome to Python ATM System")

    current_balance = 5000
    if withdrawal_amount <= 0:
        print("Error: Withdrawal amount must be greater than 0")

    elif withdrawal_amount > current_balance:
        print(f"Error: Insufficient balance. Available: {current_balance}")

    elif withdrawal_amount % 500 != 0:
        print("Error: Withdrawal amount must be multiple of 500")
    else:
        current_balance -= withdrawal_amount
        print(f"Withdrawal successful. Amount: {withdrawal_amount}"
              f" Remaining balance: {current_balance}")
        return True
    print("Thank you for using our ATM")
    return False


# Test the ATM withdrawal system
withdrawal_amount = int(input("Enter the amount to withdraw: "))
atm_withdrawal(withdrawal_amount)