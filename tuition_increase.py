#Set the cost of the semester
semester_cost = 8000
#run a loop that goes from 1 to 5
for year in range (1,6):
    #calculate the increase in by 3 percent each year
    increased_cost = semester_cost * .03
    #add increased cost to the semester cost
    semester_cost = increased_cost + semester_cost
    #print the year and increased tuition value
    print("In year ", year, ", the cost of tuition is $", format(semester_cost,".2f"), sep="")