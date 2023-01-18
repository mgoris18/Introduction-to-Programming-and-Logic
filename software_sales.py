#This program determines the discount, if applicable, and the total cost of an amount of packages purchased.

#the cost of a single package
Package_amount = 99

#Get the amount of packages purchased
packages_purchased = float(input('Enter number of packages purchased: '))

#Get the total cost of the packages purchased:
Package_total = Package_amount * packages_purchased

if (packages_purchased >= 10): #Determine whether purchase qualifies for a discount
    if packages_purchased >= 10 and packages_purchased <= 19: #Calculates discount if purchase is greater than or equal to ten and less than or equal to nineteen
        Discount = Package_total * .10 #10% discount if purchase is greater than or equal to ten
    elif packages_purchased >= 20 and packages_purchased <= 49: #Calculates discount if purchase is greater than or equal to twenty and less than or equal to forty-nine
        Discount = Package_total * .20 #20% discount if purchase is greater than or equal to twenty
    elif packages_purchased >= 50 and packages_purchased <= 99: #Calculates discount if purchase is greater than or equal to fifty  and less than or equal to ninty-nine
        Discount = Package_total * .30 #30% discount if purchase is greater than or equal to fifty
    elif packages_purchased >= 100: #Calculates discount if purchase is greater than or equal to one hundred
        Discount = Package_total * .40 #40% discount if purchase is greater than or equal to one hundred
    print('Discount: ', format(Discount,',.2f' )) #displays the discount applicable
    print('The total cost of the purchase is $', format(Package_total - Discount,',.2f' )) #displays the total amount of the pur  chase with the discount applied
else: 
        print('Your purchase does not qualify for a discount.')

