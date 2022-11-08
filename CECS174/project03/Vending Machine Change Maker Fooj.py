'''This program will request the user to purchase and item or quit, It is a vending machine change maker'''
#program starts with a stock 25 nickles, 25 dimes, 25 quarters
print("Welcome to the vending machine change maker program")
print("Change maker initialized.")
nickels=25
dimes=25
quarters=25
ones=0
fives=0


def print_stock():
    '''This function prints what stock contains'''
    print("Stock contains:")
    print(f'     {nickels} nickles')
    print(f'     {dimes} dimes')
    print(f'     {quarters} quarters')
    print(f'     {ones} ones')
    print(f'     {fives} fives')
    print()
    
def validate_price(fnum):
    '''This function gets the parameter parameter fnum and validates it if is a positive number multiple of .05, then returns a fnum which is validated'''
    #validate the price (non-negative multiple of .05)
    while fnum<0 or fnum*100 % 5 !=0:
        #print error message and ask again
        print("Illegal price: Must be a non-negative multiple of 5 cents.")
        print()
        fnum=input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    fnum=float(fnum)
    return fnum
       
#print a menu for coin/bill or cancel by c
def menu():
    '''This function prints the menu'''
    print("Menu for deposits:")

    print('{:>5}'. format("'n' - deposit a nickel"))
    print('{:>5}'. format("'d' - deposit a dime"))
    print('{:>5}'. format("'q' - deposit a quarter"))
    print('{:>5}'. format("'o' - deposit a one dollar bill"))
    print('{:>5}'. format("'f' - deposit a five dollar bill"))
    print('{:>5}'. format("'c' - cancel the purchase"))
    print()


#validate the menu
def validate_menu(deposit,price_left):
    '''This function gets the parameters deposit and price_left as a string and integer respectively, returns price_left
    deposit : 'n' => price_left -5 and adds to nickels stock by one 
    deposit : 'd' => price_left -10 and adds to dimes stock by one 
    deposit : 'q' => price_left -25 and adds to quartors stock by one 
    deposit : 'o' => price_left -100 and adds to one dollar bills stock by one 
    deposit : 'f' => price_left -500 and adds to five dollar bills stock by one 
    deposit : 'c' => process is canceled and the money deposited until then must be given back 
    if anything else => wrong entry


    '''
    #validate the deposit
    global nickels 
    global dimes
    global quarters
    global ones
    global fives

    if deposit=='n':
        price_left= price_left-5
        nickels  += 1
    
    elif deposit=='d':
        price_left= price_left-10
        dimes +=1
      
    elif deposit=='q':
        price_left= price_left-25
        quarters +=1
     
    elif deposit=='o':
        price_left= price_left-100
        ones +=1
    
    elif deposit=='f':
        price_left= price_left-500
        fives +=1

    else:
        print(f"Illegal selection: {deposit}")
    
    #print payment due
    if 0<price_left<100:
        print(f"Payment due: {price_left:.0f} cents")
    elif price_left>100:
        print(f"Payment due: {price_left//100:.0f} dollars and {price_left%100:.0f} cents") 
    else: 
        print()
        
    return price_left
        
#print the remaining amount each time
def remain(coins):
    if coins<0:
        change=-coins
    else:
        change=coins
    global nickels 
    global dimes
    global quarters

    print("Please take the change below.")

    for quarters_change in range(quarters+2):
        if quarters_change *25 > change:
            break
            
    change -= (quarters_change-1)*25
        
    for dimes_change in range(dimes+2):
        if dimes_change *10 > change:
            break
    change -=  (dimes_change-1) *10
        
    for nickels_change in range(nickels+2):
        if nickels_change*5 > change:
            break
    change -= (nickels_change-1) * 5
    
    quarters_change -=1
    dimes_change -=1
    nickels_change -=1
            
    if quarters_change >0 :
        print(f"     {quarters_change} quartors")
        quarters -=quarters_change
    if dimes_change >0 :
        print(f"     {dimes_change} dimes")
        dimes -=dimes_change
    if nickels_change >0 :
        print(f"     {nickels_change} nickels")
        nickels -=nickels_change

  
    if change!=0:
        print("Machine is out of change")
        print("See store manager for remaining refund")
        if 0<change<100:
            print(f"Amount due: {change:.0f} cents")
        else:
            print(f"Amount due: {change//100:.0f} dollars and {change%100:.0f} cents") 

#main program

print_stock()
price=input("Enter the purchase price (xx.xx) or 'q' to quit: ")
#ask the user input repeatedly until q
while price!='q':
    
    fprice=float(price)
    final_price=validate_price(fprice)
    print()
    menu()

    allcents=final_price*100
    dollars=allcents//100
    cents=allcents % 100
    if 0<allcents<100:
        print(f"Payment due: {allcents:.0f} cents")
    else:
        print(f"Payment due: {dollars:.0f} dollar(s) and {cents:.0f} cents")

    while allcents>0:
        menus=input("Indicate your deposit: ")
        if menus=='c':
            allcents = final_price * 100 - allcents
            print()
            break
        allcents=validate_menu(menus, int(allcents))
    
            
    remain(allcents)
    if allcents==0:
        print("     No charge due.") 
    print()
    print_stock()
    price=input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    
total = nickels*5 + dimes*10 + quarters*25 + ones*100 + fives*500
print()
print(f"Total: {total//100:.0f} dollars and {total%100:.0f} cents") 

