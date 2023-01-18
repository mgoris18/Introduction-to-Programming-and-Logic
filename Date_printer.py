#This function will take in a date input in mm/dd/yyyy format 
# and print it in mm dd, yy format

#define the main function
def main():
    #get the date input in mm/dd/yyyy format
    date = input('Enter the date in the mm/dd/yyyy format: ')
    #set mm to equal the first two characters in the date string
    mm = date[0:2]
    #if mm input is 1 then month is january
    if mm == '01':
        month = 'January'
    #if mm input is 2 then month is February
    elif mm == '02':
        month = 'February'
    #if mm input is 3 then month is March
    elif mm == '03':
        month = 'March'
    #if mm input is 4 then month is April
    elif mm == '04':
        month = 'April'
    #if mm input is 5 then month is May
    elif mm == '05':
        month = 'May'
    #if mm input is 6 then month is June
    elif mm == '06':
        month = 'June'
    #if mm input is 7 then month is July
    elif mm == '07':
        month = 'July'
    #if mm input is 8 then month is August
    elif mm == '08':
        month = 'August'
    #if mm input is 9 then month is September
    elif mm == '09':
        month = 'September'
    #if mm input is 10 then month is October
    elif mm == '10':
        month = 'October'
    #if mm input is 11 then month is November
    elif mm == '11':
        month = 'November'
    #if mm input is 12 then month is December
    elif mm == '12':
        month = 'December'
        #print in proper format
    print (month, date[3:5]+ ',', date[6:10])
    return date
main()

