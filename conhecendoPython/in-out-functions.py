## Read String

##name = input("Tell me your name: ")

##print(f"Hello, {name}")


## Some tests by me...

"""ACCOUNT_BALANCE, USER_NAME, ACCOUNT_PASSWORD = 12450.79, "Abraham Santos", 200401

while True:  # Main loop to keep returning to the start
    password = float(input("Type your password: "))

    if password == ACCOUNT_PASSWORD:
        print(f"Welcome, Sr. {USER_NAME}! \n Your account balance is {ACCOUNT_BALANCE}")

        while True:  # Loop for operations and post-operation options
            print("What do you want to do?")
            option = input(" 1 - Withdraw \n 2 - Deposit \n 3 - Transfer \n 4 - Exit \n")

            def perform_operation(option_code):
                global ACCOUNT_BALANCE  # Access global variable

                if option_code == "1":
                    withdraw = float(input("Enter the value you want to withdraw: "))
                    ACCOUNT_BALANCE -= withdraw
                    print(f"Your current balance is {ACCOUNT_BALANCE}")

                elif option_code == "2":
                    deposit = float(input("Enter the value you want to deposit: "))
                    ACCOUNT_BALANCE += deposit
                    print(f"Your current balance is {ACCOUNT_BALANCE}")

                elif option_code == "3":
                    transfer = float(input("Enter the value you want to transfer: "))
                    ACCOUNT_BALANCE -= transfer
                    print(f"Your current balance is {ACCOUNT_BALANCE}")

                else:
                    print("Invalid option! Try again...")

            if option != "4":
                perform_operation(option)

                while True:
                    post_operation = input("What do you want to do now? \n 1 - Close \n 2 - Return to Start \n")
                    if post_operation == "1":
                        print(f"Goodbye, {USER_NAME}!")
                        break  # Exit the inner loop (close)
                    elif post_operation == "2":
                        break  # Exit the inner loop (return to start)
                    else:
                        print("Invalid option! Try again...")
            else:
                print(f"Goodbye, {USER_NAME}!")
                break  # Exit the outer loop (exit program)

    else:
        print("Wrong password! Check the entry and try again...")"""