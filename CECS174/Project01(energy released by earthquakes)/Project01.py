#start of the program
'''This program evaluates energy in joules and TNT in tons by given richter'''

#printing Richter , Joules and TNT as in a table formatting with string alignment

#calculating energy and tons for 5 values of 1, 5, 9.1, 9.2, 9.5
richter1 = 1
energy1 = 10**((1.5*richter1)+4.8)
tons1 = energy1/(4.184 * 10**9)

richter5 = 5
energy5 = 10**((1.5*richter5)+4.8)
tons5 = energy5/(4.184 * 10**9)

richter9_1 = 9.1
energy9_1 = 10**((1.5*richter9_1)+4.8)
tons9_1 = energy9_1/(4.184 * 10**9)

richter9_2 = 9.2
energy9_2 = 10**((1.5*richter9_2)+4.8)
tons9_2 = energy9_2/(4.184 * 10**9)

richter9_5 = 9.5
energy9_5 = 10**((1.5*richter9_5)+4.8)
tons9_5 = energy9_5/(4.184 * 10**9)

#putting the variables in a way to print them out 
  
Richter = [
    ['Richter', 'Joules', 'TNT'],
    [richter1, energy1, tons1],
    [richter5, energy5, tons5],
    [richter9_1, energy9_1, tons9_1],
    [richter9_2, energy9_2, tons9_2],
    [richter9_5, energy9_5, tons9_5]
]
#https://scientificallysound.org/2016/10/17/python-print3/
#used this website to help with the alignments 
print('{:<14} {:>7} {:>23} '. format(Richter[0][0], Richter[0][1], Richter[0][2]))

print('{:<10} {:>4} {:>36} '. format(Richter[1][0], Richter[1][1], Richter[1][2]))
print('{:<10} {:>4} {:>30} '. format(Richter[2][0], Richter[2][1], Richter[2][2]))
print('{:<10} {:>4} {:>20} '. format(Richter[3][0], Richter[3][1], Richter[3][2]))
print('{:<10} {:>4} {:>20} '. format(Richter[4][0], Richter[4][1], Richter[4][2]))
print('{:<10} {:>4} {:>19} '. format(Richter[5][0], Richter[5][1], Richter[5][2]))


print()
#ask user for a float richter value
#evaluate the energy and tons and print the values as asked

richter_user = float(input('Please enter a Richter scale value: '))
energy = 10**((1.5*richter_user)+4.8)
tons = energy/(4.184 * 10**9)
print('Richter scale value: ', richter_user)
print('Equivalence in joules: ', energy)
print('Equivalence in tons of TNT: ', tons)
