def school_fee_tracker():
    outstanding_balance = 8000  # Initial semester balance

    while outstanding_balance > 0:
        try:
            payment = float(input("Enter amount to pay: $"))

            if payment <= 0:
                print("Please enter a valid positive amount.")
                continue

            if payment > outstanding_balance:
                extra = payment - outstanding_balance
                outstanding_balance = 0
                print(
                    f"Payment successful! You have overpaid by ${extra}. Your outstanding balance is $0.")
                print(
                    f"Please contact the school office for a refund or adjustment of the extra amount.")
                break
                continue

            outstanding_balance -= payment
            print(
                f"Payment successful! Remaining balance: ${outstanding_balance}")

            if outstanding_balance == 0:
                print("All fees paid. You have no outstanding balance.")
                break

        except ValueError:
            print("Invalid input! Please enter a numerical value.")


school_fee_tracker()
