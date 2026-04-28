grades_counter = 1
grade_pass = 0
grade_fail = 0
avg_pass = 0
avg_fail = 0
total_avg = 0
total_grades = (int(input('Please enter number of grades to be processed: ')))

while grades_counter <= total_grades:
    grade = int(input(f'Please enter the score of your {grades_counter} grade: '))
    grades_counter += 1
    total_avg = int(grade / total_grades) + total_avg
    if grade > 70:
        grade_pass += 1
        avg_pass += grade
    else:
        grade_fail += 1
        avg_fail += grade

if grade_pass >= 1:
    avg_pass = int(avg_pass / grade_pass)
else:
    avg_pass = 0

if grade_fail >= 1:
    avg_fail = int(avg_fail / grade_fail)
else:
    avg_fail = 0

print(f'The total average is {total_avg}') 
print(f'The number of passing grades is {grade_pass}, and their average is {avg_pass}')
print(f'The number of failing grades is {grade_fail}, and their average is {avg_fail}')