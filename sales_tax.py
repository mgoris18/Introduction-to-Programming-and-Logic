purchase_amount = float(input('Enter amount of purchase: ')) 

state_tax_total = purchase_amount * 0.05 

county_tax_total = purchase_amount * 0.025

total_tax = state_tax_total + county_tax_total

sale_total = total_tax + purchase_amount

print('The amount of the purchase is $', format(purchase_amount,',.2f' ))
print('The amount of the state tax is $', format(state_tax_total,',.2f' ))
print('The amount of the county tax is $', format(county_tax_total,',.2f' ))
print('The total tax is $', format(total_tax,',.2f' ))
print('The sale total is $', format(sale_total,',.2f' ))


