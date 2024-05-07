def show_items():
    print ("Welcome to the Vending Machine!")
    
    print ("1.Flamin' Hot Cheetos - 3 DHS")
    print ("2.Pepsi- 2.50 DHS")
    print ("3.Sprite- 2 DHS")
    print ("4.Mirinda- 2 DHS")
    print ("5.Mr.Krisps- 1.50 DHS")
    print ("6.Super Ring- 1 DHS")
    print ("7.Salad- 2 DHS")
    print ("8.Bugles- 17 DHS")
    print ("9.Exit")

def get_choice():
    selection = int (input ("Enter the Number of your Selection: "))
    
    if selection == 1:
        return "Flamin' Hot Cheetos"
    
    elif selection == 2:
        return "Mountain Dew"
    
    elif selection == 3:
        return "Sprite"
    
    elif selection == 4:
        return "Chocolate Biscuit"
    
    elif selection == 5:
        return "Ice Cream Sandwich"
    
    elif selection == 6:
        return "Maltesers"
    
    elif selection == 7:
        return "Lays Chips"
    
    elif selection == 8:
        return "Water"
    
    elif selection == 9:
        return "Exit"
    
    else:
        print ("Invalid selection. please try again.")
        return get_choice ()

def handle_payment (product):
    print ("selected item:", product)
    
    amount = float (input ("Insert Money: "))
    
    cost = 0.0
    
    if product == "Water" or product == "Lays Chips" or product == "Mountain Dew" or product == "Sprite":
        cost = 2
    
    elif product == "Ice Cream Sandwich":
        cost = 2.50
    
    elif product == "Chocolate Biscuit":
        cost = 1.75
    
    elif product == "Malteasers":
        cost = 3.50
    
    elif product == "Flamin' Hot Cheetos":
        cost = 4
    
    if amount >= cost:
        balance = amount-cost
        print ("payment successful!here's your change: ", balance , "DHS")
    
    else:
        print ("Insufficient payment.please try again.")
        handle_payment (product)

def start_vending_machine():
    while True:
        show_items()
        product = get_choice()
        
        if product == "Exit":
            print ("Thank you for using the Vending Machine!")
            
            break
        
        else:
            handle_payment (product)

start_vending_machine()
