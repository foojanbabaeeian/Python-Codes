import math

''' The program will ask for three inputs, 
including Customer's code, beginning meter reading and ending meter reading respectively'''

customer_code = input("Enter the customer's code: ")
begin = int(input("Enter the customer's beginning meter reading: "))
end = int(input("The customer's ending meter reading:          "))


# It will compute the gallons of water used by the customer
'''The meter has nine digits'''
distance = end - begin
if end < begin:
    distance = 10e8 - math.fabs(end - begin)
water_g = distance / 10

# compute the amount of money that the customer wil be billed, based on customer's code and water usage
'''
Code r => residential 5 dollars plus 0.0005 per gallon used
Code c=> commercial 1000.00 for 4 million gallons or less and 0.00025 for each extra gallon
Code i=> industrial 1000.00 less than 4 million gallons
                    2000.00 between 4 and ten
                    2000.00 + 0.00025 for each extra after 10 
'''

print()
print("Customer code:", customer_code)
print("Beginning meter reading:", "{:0>9}".format(begin))
print("Ending meter reading:   ", "{:0>9}".format(end))


bill = 0
if (0 < begin < 10e8) and (0 < end < 10e8):
    if customer_code == 'R' or customer_code == 'C' or customer_code == 'I' or customer_code == 'r' or customer_code == 'c' or customer_code == 'i':
        if customer_code == 'R' or customer_code == 'r':
            bill = 5 + (0.0005 * water_g)
        elif customer_code == 'C' or customer_code == 'c':
            if water_g <= 4 * 10e5:
                bill = 1000
            else:
                bill = 1000 + (0.00025 * (water_g - (4 * 10e5)))
        elif customer_code == 'I' or customer_code == 'i':
            if water_g <= 4 * 10e5:
                bill = 1000
            elif 4 * 10e5 < water_g < 10e6:
                bill = 2000
            else:
                bill = 2000 + (0.00025 * (water_g - 10e6))
    else:
        water_g = 0
        print('Invalid Entry')
else:
    water_g = 0
    print('Invalid Entry')

'''
Outputs: 
Customer's code
begin
end
gallons of water
amount of money
'''


print("Gallons of water used:", f'{water_g:.1f}')
print("Amount billed:", f'${bill:.2f}')
print()
