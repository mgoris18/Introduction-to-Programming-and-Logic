# This program will store correct answers to an exam in a list,
# It will store the answers of the students in another list, 
# And will display the results of the exam

#Define the correct answers function
def correct_answers():
    #set correct_answers as a list with the correct answers given
    correct_answers_list = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B','D', 'A',]
    #return list
    return correct_answers_list
#define student answers function
def student_answers():
    #set variable
    student_answers_list = []
    #open file for reading
    outfile = open('answers.txt', 'r')
    #for loop
    for i in outfile:
        #remove new lines
        i = i.rstrip('\n')
        #append to list
        student_answers_list.append(i)
    #return list
    return student_answers_list
#Define function to check answers based on the correct answer list and the student answers list.
def answers_check(correct_answers_list, student_answers_list):
    #initialize variable to keep count of numbers
    count = 0
    #print correct answers list
    print(correct_answers_list)
    #print student answers list
    print(student_answers_list)
    #set incorrect answers variable
    incorrect_answers = []
    #set for loop in a range of 20 answers
    for i in range(20):
        #If the correct answer and the student answer are the same add 1 to count
        if correct_answers_list[i] == student_answers_list[i]:
            count += 1
        #if the correct answer and the student answer are not the same, add 0 to count and store the number in incorrect answers list
        else: 
            incorrect_answers.append(i)
            count += 0
    #if count is less than 15 then print 'you have failed the exam'
    if count < 15:
        print('You have failed the exam')
    #if count is greater than 15, then print 'congratulations, you have passed the exam'
    else: 
        print('Congratulations! You have passed the exam')
    #print correct answers amount, incorrect answers amount, and which questions were incorrect
    print('You answered ', count, 'questions correctly')
    print('You answered ', 20 - count, 'questions incorrectly')
    print('The following questions were incorrect: ' , incorrect_answers)
    #return function
    return answers_check   
#define main function
def main():
    #set correct answers list to equal correct answers function
    correct_answers_list = correct_answers()
    #set students answers list to equal student answers function
    student_answers_list = student_answers()
    #set answers check to be based on correct answers list and student answers list
    answers_check(correct_answers_list, student_answers_list)
main()


