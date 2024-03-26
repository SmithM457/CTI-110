#Matthew Howe
#3/26/24
#P3HW1
#This program will determine the letter grade for a student

#This program takes a number grade, determines average and displays letter grade for average

#Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

#Add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

#Determine lowest, highest, sum, and average for grades
print()
print('------------Results------------')

low = min(grades)
high = max(grades)
sum1 = sum(grades)
avg = sum1/len(grades)

print('Lowest Grade:'.ljust(20) + str(format(low,'.1f')))
print('Highest Grade:'.ljust(20) + str(format(high,'.1f')))
print('Sum of Grades:'.ljust(20) + str(format(sum1,'.1f')))
print('Average:'.ljust(20) + str(format(avg,'.2f')))
print('-'*30)

#Determine letter grade for average

if avg >= 90:
    print('Your grade is: A')
else:
    if avg >= 80:
        print('Your grade is: B')
    else:
        if avg>= 70:
            print('Your grade is: C')
        else:
            if avg >= 60:
                print('Your grade is: D')
            else:
                if avg >= 50:
                    print('Your grade is: F')
