#This program accepts two integers and returns the value that is greater

 #Accept inputs
a = int(input('Input your first value: '))
b = int(input('Input your second value: '))
#function is called max
def max(a, b) :
    #if a is greater than b, return a
    if a >= b:
        return a
    #if a is not greater than b, return b
    else:
        return b
max(a,b)
#print greater value
def results():
    print('The greater value is: ', format(max(a, b), ',.2f'), sep="")
results()
