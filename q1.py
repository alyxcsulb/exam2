# revised answer for midterm 2 from lecture
# removed def function, no more type error either


import os
import sys 

READ_FILE_NAME = 'scores.txt'
READ_MODE = 'r'
WRITE_FILE_NAME = 'grades.txt'
WRITE_MODE = 'w'
STUDENT_COUNT = 0
GRADE = ''
GPA = ''
AVG_GPA = 0
TOTAL_GPA = 0

try:
    scores_file = open(READ_FILE_NAME, READ_MODE)
    grades_file = open(WRITE_FILE_NAME, WRITE_MODE)
    with scores_file,grades_file:
        for line in scores_file:
            x_firstname, x_lastname, x_score = line.split()

            try:
                if int(x_score) >= 90:
                    GRADE = 'A'
                    GPA = 4.0
                elif int(x_score) >= 80:
                    GRADE = 'B'
                    GPA = 3.0
                elif int(x_score) >= 70:
                    GRADE = 'C'
                    GPA = 2.0
                elif int(x_score) >= 60:
                    GRADE = 'D'
                    GPA = 1.0
                elif int(x_score) < 60:
                    GRADE = 'F'
                    GPA = 0.0

                TOTAL_GPA += GPA

                #write data to file
                grades_file.write(f'{x_firstname} {x_lastname} {GRADE} \n')

            except ValueError as error:
                print(f'Bad score value for {x_firstname} {x_lastname}, ignored.\n')
            else:
                STUDENT_COUNT += 1 #counts the no of records in file if no value error exists
        
        #average gpa of valid records
        AVG_GPA = (TOTAL_GPA/STUDENT_COUNT)

        grades_file.write(f'\nThe class GPA is {AVG_GPA:.2f}')
        print(f'The class GPA is {AVG_GPA:.2f}')

#handling exceptions
except OSError as error:
    print(f'Unable to open file {READ_FILE_NAME}. Error message: {error}')
except:
    error = sys.exc_info()[0] # to get error info
    print(f'Unexpected error: {error}')
finally:
    print('Finally code block executed.')