#day 2 of 100 days of code building tip claculators...

def calculate_tip():
    """
    This function takes no parameters but utilizes imputs to enhance the user experience
    """
    print("welcome to the tip calculator!")

    total_bill = int(input("what was the total_bill? : "))
    percent_tip = int(input("how much percentage tip would you like to leave?: "))
    party_size = int(input("how many people will be splitting the cost"))

    tip = (total_bill * (percent_tip/100))/party_size

    print(f"each person should leave a tip of ${tip}")


calculate_tip()


def easy_tip(total_bill, percentage_tip = 20, party_size = 1):
    """
    Here the user of the function has the option to enter the total bill and update parmeters 
    or choose to use default values
    """
    print("Welcome to the tip calculator")
    total_bill = total_bill
    tip = (total_bill * (percentage_tip/100))/party_size

    print(f"everyone should leave ${tip} as a tip")

#using parameters and default values to calulate tip in a different way
easy_tip(350, 18, 2)



    
    