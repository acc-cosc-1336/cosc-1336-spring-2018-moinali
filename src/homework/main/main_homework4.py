#write the import statements to bring in homework 4 functions
#valid_letter_grade, get_credit_points, get_grade_points, and get_grade_point_average
from src.homework.homework4 import valid_letter_grade
from src.homework.homework4 import get_credit_points
from src.homework.homework4 import get_grade_points
from src.homework.homework4 import get_grade_point_average

'''
Use the functions from homework4 to...
Write code to prompt the user for number of students and grades.
Create a nested loop to collect letter grades and credit hours for each student.
Vaidate the letter grade is in accepted range if not prompt user for letter again.
From the letter grade, get the credit points for that class.
Calculate grade points (How? Research GPA calculation).
Sum grade points and credit hours for each student.
Calculate GPA for each student.
Display Student 1(etc) GPA is 3.77. Format the GPA to two values.
'''

#WRITE YOUR CODE IN THE MAIN FUNCTION BELOW
def main():
    num_students =  int(input("Enter the number of students: "))
    num_grades = int(input("Enter the number of grades per student: "))

    for student in range(1, num_students+1):
        total_grade_points = 0.0
        total_credit_hours = 0.0

        for class_num in range(1, num_grades+1):
            print ('For Student', student, ', Class ', class_num, ' enter a grade', end='')
            letter_grade = input(':')
            
            valid = valid_letter_grade(letter_grade)
            while valid == False:
                print ('Invalid Letter Grade')
                letter_grade = input('enter a grade: ')
                valid = valid_letter_grade(letter_grade)

            
            print ('How many credit hours for Class ', class_num)
            credit_hours = float(input(': '))
            credit_points = float(get_credit_points(letter_grade))
            
            grade_points = get_grade_points(credit_hours, credit_points)

            total_credit_hours += credit_hours           
            
            total_grade_points += grade_points
            

        gpa = get_grade_point_average(total_credit_hours, total_grade_points)
        print ('Student ', student, ' GPA is ', format(gpa, '.2f'))
main()        
