#define main fuction
def main():
    #set letters list
    alphabet = ['A', 'B' ,'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J' ,'K', 
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    #set list with numbers that match letters
    numbers = ['2', '2', '2', '3', '3', '3', '4', '4', '4', '5','5','5','6','6','6','7','7','7'
    ,'8','8','8','9','9','9', '9']
    
    #accept phone number input
    phone_number = input('Enter phone number in XXX-XXX-XXXX format: ').upper()
    #set count to zero
    count = 0
    #For loop
    for count in range(len(phone_number)):
        #if there is a letter in the inputted number print it with it's number equivalent
        if phone_number[count].isalpha():
            print(numbers[alphabet.index(phone_number[count])], end = '')
        #Else return the phone number
        else:
            print(phone_number[count], end = '')
#Close function
main()
