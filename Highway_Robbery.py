#This program will calculate automolibe liability insuarance estimates
#function main

#Control the loop
continue_calculator = 'y'

def main():
    global continue_calculator
    while continue_calculator == 'y':
    #Accept name, age, and number of traffic violations of customer
        print()
        customer_name = (input('Enter name: '))
        customer_age = int(input('Enter age: ')) 
        invalid_age(customer_age)
        traffic_violations = int(input('Enter number of traffic violations: '))
        print()

        #define codes 
        code1 = 'high risk'
        code2 = 'moderate risk'
        code3 = 'low risk'
        code4 = 'no risk'
        #determine risk level case
        if traffic_violations == 0:
            risktype = code4
        elif traffic_violations == 1:
            risktype = code3
        elif traffic_violations == 2 or traffic_violations == 3:
            risktype = code2
        else:
            risktype = code1
        
        #determine insurance princing based on age of customer and number of trafic violations
        if customer_age < 25 and risktype == code1:
            price = 480
        elif customer_age >= 25 and risktype == code1:
            price = 410
        elif customer_age < 25 and risktype == code2 and traffic_violations == 3:
            price = 450
        elif customer_age >= 25 and risktype == code2 and traffic_violations == 3:
            price = 390
        elif customer_age < 25 and risktype == code2 and traffic_violations == 2:
            price = 405
        elif customer_age >= 25 and risktype == code2 and traffic_violations == 2:
            price = 365
        elif customer_age < 25 and risktype == code3:
            price = 380
        elif customer_age >= 25 and risktype == code3:
            price = 315
        elif customer_age < 25 and risktype == code4:
            price = 325
        else:
            price = 275

        invalid_violations(traffic_violations)
        quote(customer_name, price, customer_age, risktype)
        print()
        continue_calculator = input('Would you like another quote? Enter y if yes: ')

def invalid_age(customer_age):
    #Return an error message if age is outside range
    while customer_age < 16 or customer_age > 105:
        print()
        print('INVALID: Driver must be between 16 and 105 years of age')
        print()
        customer_age = int(input('Enter age: ')) 

def invalid_violations(traffic_violations):
    #Return an error message if amount of traffic violations is outside range
    while traffic_violations < 0:
        print()
        print('INVALID: Violations cannot be less than 0')
        print()
        traffic_violations = int(input('Enter number of traffic violations: '))


        #define quote function
def quote(customer_name, price, customer_age, risktype):
        print(customer_name,', as a ', risktype, ' driver, your insurance will cost $', format(price, '.2f'), sep="")



main()
