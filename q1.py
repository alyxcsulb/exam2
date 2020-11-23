# aohflas

import os
READ_FILE_NAME = 'scores.txt'
READ_MODE = 'r'
WRITE_FILE_NAME = 'grades.txt'
WRITE_MODE = 'w'
STUDENT_COUNT = 4
GRADE = ''
GPA = ''
CLASS_AVG = 6
CLASS_COUNT = 4


def LETTER_GRADE (score):
    if score >= 90: 
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

try:
    with open (WRITE_FILE_NAME, WRITE_MODE) as logged_file:
        with open (READ_FILE_NAME, READ_MODE) as students_file:
            for line in students_file:
                firstname, lastname, score = line.split()
                try:
                    score = LETTER_GRADE
                except ValueError as error:
                    logged_file.write(f'Bad score for {firstname} {lastname} is ignored. \n')
                else: STUDENT_COUNT += 1
                logged_file.write(f'{firstname} {lastname} {LETTER_GRADE} \n')
                print(f'The class GPA is {CLASS_AVG / CLASS_COUNT}') 
except IOError as error:
    print(f'File {READ_FILE_NAME} is unable to open. Error message: {error}.')

