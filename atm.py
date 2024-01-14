import sys
from tabulate import tabulate


def main():
    start()


def start(balance=50000):
    username = str(input("Enter username to sign in: "))
    header = [f"Welcome {username}, How may I help you?", "Codes"]
    table = [
        ["Withdraw Money", "W"],
        ["Deposit Money", "D"],
        ["Check Balance", "B"],
        ["Transfer Money", "T"],
        ["Recharge", "R"],
        ["Quit", "Q"],
    ]

    t = tabulate(table, headers=header, tablefmt="grid")
    print(t)

    while True:
        code = str(input("Enter a transaction code:\n "))

        if code.upper() == "Q":
            sys.exit("Transaction Cancelled❌\nThank you for banking with us 👍")

        if code not in ["W", "w", "D", "d", "B", "b", "T", "t", "R", "r"]:
            print("Invalid transaction code")

        elif code.upper() == "W":
            withdraw(balance)
        elif code.upper() == "D":
            deposit(balance)
        elif code.upper() == "B":
            get_balance(balance)
        elif code.upper() == "T":
            transfer(balance)
        elif code.upper() == "R":
            recharge(balance)


def withdraw(balance):
    while True:
        try:
            amount = float(input("Enter amount to withdraw: ₦"))
            if float(balance) > amount:
                balance -= amount
                print("Please take your cash 💵")
                break
            else:
                print("Insufficient funds")
        except (TypeError, Exception):
            print("Please enter a valid input: ")

    continue_or_cancel(balance)


def deposit(balance):
    while True:
        try:
            amount = float(input("Enter amount to deposit: ₦"))
            if amount <= 0:
                print("Deposit amount must be greater than zero")
            else:
                print(f"₦{amount:.2f} has been added to your balance! ✔️")
                break
        except (TypeError, ValueError, Exception):
            print("Invalid amount")

    continue_or_cancel(balance)


def get_balance(balance):
    account_balance = [[f"  ₦{balance:.2f}k  "]]
    header = ["Current Balance"]
    print(tabulate(account_balance, headers=header, tablefmt="grid"))
    continue_or_cancel(balance)


def transfer(balance):
    banks = [
        ["FirstBank", "FB"],
        ["Fidelity", "F"],
        ["Palmpay", "PA"],
        ["OPay", "OP"],
        ["EcoBank", "E"],
        ["UBA", "UBA"],
        ["Access", "A"],
        ["GTB", "GTB"],
        ["Union Bank", "U"],
        ["KUDA", "KU"],
        ["Zenith Bank", "Z"],
        ["KeyStone", "KY"],
        ["Others", "O"],
        ["Unity", "U"],
    ]
    bank_headers = ["Banks", "Codes"]
    bank_codes = [
        "FB",
        "F",
        "PA",
        "OP",
        "E",
        "UBA",
        "A",
        "GTB",
        "U",
        "KU",
        "Z",
        "KY",
        "O",
        "U",
    ]
    print(tabulate(banks, headers=bank_headers, tablefmt="grid"))
    while True:
        try:
            bank = str(input("Please select the bank you want to transfer to: "))
            if bank.upper() == "O":
                bank = str(input("Enter the name of the bank: "))
            recipient_acc = str(int(input("Recipient account number: ")))
            amount = int(input("Amount to transfer: ₦"))
            pin = str(input("Enter your PIN: "))

            if bank or recipient_acc or amount or pin in ["Q", "q"]:
                sys.exit("Transaction Cancelled❌\nThank you for banking with us 👍")

            if len(pin) != 4 or not pin.isdigit():
                print("Incorrect PIN ❌")
             
            if amount <= 0:
                print("Amount must be greater than zero ❌")
            if bank.upper() in bank_codes and len(str(recipient_acc)) == 10:
                if balance > amount:
                    balance -= amount
                    print("Transfer successful ✔️")
                    break

        except (TypeError, ValueError):
            print("Invalid bank selected")
    continue_or_cancel(balance)


def recharge(balance):
    networks = [["Glo", "G"], ["Airtel", "A"], ["MTN", "M"], ["9Mobile", "9"]]
    codes = ["G", "A", "M", "9"]
    network_headers = ["Networks", "Codes"]
    networks_table = tabulate(networks, headers=network_headers, tablefmt="outline")
    print(networks_table)
    while True:
        try:
            code = str(input("Select network code: "))
            phone_number = str(input("Enter the phone number you want to recharge: "))
            recharge_amount = int(input("Enter amount: "))

            if code.upper() or phone_number.upper() or recharge_amount in ["Q", "q"]:
                sys.exit("Transaction Cancelled❌\nThank you for banking with us 👍")

            if code.upper() not in codes:
                print("Invalid Code")
            if len(phone_number) != 11 or not phone_number.isdigit():
                print("Please enter a valid phone number")
            if code.upper() in codes and len(phone_number) == 11:
                if balance > recharge_amount:
                    balance -= recharge_amount
                    print(f"Recharge of ₦{recharge_amount} is successful! ✔️")
                    break
                print("Insufficient funds.\nDeposit money into your account.")
        except (ValueError, TypeError):
            print("Invalid Input")
    continue_or_cancel(balance)


def continue_or_cancel(balance):
    try:
        to_continue = str(input("Do you want to perform another transaction? (Y/N): "))
    except Exception:
        print("Invalid input")
    if to_continue.upper() == "Y":
        start(balance)
    sys.exit("Thank you for banking with us 👍")


if __name__ == "__main__":
    main()
