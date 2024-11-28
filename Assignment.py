import random

my_list=["1","56","4","56","75","93","1","94","2","15"]

# Q1

# def list_function():
#     new_set=set(my_list)
#     changed_set=list(new_set)
#     print(changed_set)
# list_function()


# Q2
# def sort_identification():
#     if my_list==sorted(my_list):
#         print(True)
#     else:
#         print(False)
# sort_identification()

# Q3

# def display_numbers():
#     user_input1=int(input("First number"))
#     user_input2=int(input("Second number"))
#     if user_input1%7 == 0 and user_input2%7 != 0:
#         print(user_input2)
#     elif user_input1% 7 != 0 and user_input2%7 == 0:
#         print(user_input1)
#     elif user_input1% 7 != 0 and user_input2%7 != 0:
#         print(user_input1,user_input2)
#     else:
#         print("Both numbers are divisible by 7")
# display_numbers()

# Q4
# def max_number():
#     numbering=[int(input("Enter number 1: ")),
#                int(input("Enter number 2: ")),
#                int(input("Enter number 3: ")),
#                int(input("Enter number 4: ")),
#                int(input("Enter number 5: "))]
#     number_list=[]
#     for number in numbering:
#         number_list.append(number)
#     print("The max number is:",max(number_list))
# max_number()

# Q5
def sim_tool_kit():
    print("""
    1. Sim1
    2. Sim2
    """)
    user_input1=int(input("Enter your choice: "))
    if user_input1==1:
        print("Sim1")
        print("""
        1. Safaricom
        2. M-PESA
        """)
        user_input2=int(input("Enter your choice: "))
        if user_input2==1:
            print("""
            f
            """)
        else:
            print("""
            1. Send Money
            2. Withdraw Cash
            3. Buy Airtime
            4. Loans and Savings
            5. Lipa na M-PESA
            6. My Account
            7. M-PESA Agent
            0. Back
            """)
            user_input3=int(input("Enter your choice: "))
            if user_input3==1:
                print("Add a valid number")
                number = int(input())
                if number > 1000000 :
                    print("Enter Amount")
                    amount=int(input())
                    if amount > 0:
                        print("Are you sure you want to send money?")
                        print("""
                        1. Yes
                        2. No
                        """)
                        user_input4=int(input("Enter your choice: "))
                        if user_input4==1:
                            print("Money sent successfully")
                        else:
                            print("Transaction cancelled")
                    else:
                        print("Add amount")
            elif user_input3==2:
                print("Withdraw Cash")
                print("""
                1. Withdraw from ATM
                2. Withdraw from M-PESA Agent
                """)
                user_input5=int(input("Enter your choice: "))
                if user_input5==1:
                    print("ATM")
                    print("Enter Amount")
                    amount=int(input())
                    if amount > 0:
                        print("Are you sure you want to withdraw money?")
                        print("""
                        1. Yes
                        2. No
                        """)
                        user_input6=int(input("Enter your choice: "))
                        if user_input6==1:
                            code=[246,498,5497,34387,7551,75509,758573,786,8744,7599,957950,75743]
                            print("Your atm code is" ,random(code))
                        else:
                            print("Withdrawal cancelled")
                    else:
                        print("Add an amount")
                else:
                    print("M-PESA Agent")
                    user_input7=int(input("Enter Agent Number"))
                    if user_input7>100000:
                        print("Enter Amount")
                        amount=int(input())
                        if amount > 0:
                            print("Are you sure you want to withdraw money?")
                            print("""
                            1. Yes
                            2. No
                            """)
                            user_input8=int(input("Enter your choice: "))
                            if user_input8==1:
                                print(amount ,"sent to Agent")
                            else:
                                print("Withdrawal cancelled")
                        else:
                            print("Add an amount")
                    else:
                        print("Invalid Agent Number")
            elif user_input3==3:
                print("""
                1. My phone
                2. Other phone
                """)
                user_input9=int(input("Enter your choice: "))
                if user_input9==1:
                    print("My phone")
                    user_input10=int(input("Enter amount"))
                    if user_input10>0:
                        print("Airtime purchased successfully")
                    else:
                        print("Add an amount")
                elif user_input9==2:
                    print("Other phone")
                    user_input11=int(input("Enter phone number"))
                    if user_input11>100000:
                        print("Enter amount")
                        user_input12=int(input())
                        if user_input12>0:
                            print("Airtime purchased successfully")
                        else:
                            print("Add an amount")
                    else:
                        print("Invalid phone number")
                else:
                    print("Invalid choice")
            elif user_input3==4:
                print("""
                1. M-Shwari
                2. KCB M-Pesa
                """)
                user_input13=int(input("Enter your choice: "))
                if user_input13==1:
                    print("M-Shwari")
                    print("Activate")
                    user_input14=input("Re-write Activate")
                    if user_input14=="Activate":
                        print("M-Shwari activated")
                    else:
                        print("Invalid Input")
                elif user_input13==2:
                    print("KCB M-Pesa")
                    print("Activate")
                    user_input15=input("Re-write Activate")
                    if user_input15=="Activate":
                        print("M-Shwari activated")
                    else:
                        print("Invalid Input")
                else:
                    print("Invalid choice")
            elif user_input3==5:
                print("Lipa na M-Pesa")
                print("""
                1.Pay Bill
                2.Buy Goods And Services
                3.Pochi La Biashara
                """)
                user_input16=int(input("Enter your choice: "))
                if user_input16==1:
                    print()

sim_tool_kit()