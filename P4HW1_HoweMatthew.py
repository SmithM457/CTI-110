# Matthew Howe
# 4/18/24
# P4HW1
# Loop a program and put into list
choice = 'yes'
while choice.lower() == 'yes':
    
    num = int(input("How many scores do you want to enter? "))
    total = 0
    grade_list = []
    for i in range(1,num + 1):
        grade = float(input("Enter grade #" + str(i) + ": "))
        while grade < 0 or grade > 100:
            print()
            print("INVALID score entered")
            print("Score should be between 0 and 100")
            print()
            grade = float(input("Enter score #" + str(i) + " again: "))
        grade_list.append(grade)
    lowest = min(grade_list)
    grade_list.remove(lowest)
    ave = sum(grade_list)/len(grade_list)
    print(ave)
    if ave >= 90:
        letter = "A"
    elif ave >= 80:
        letter = "B"
    elif ave >= 70:
        letter = "C"
    elif ave >= 60:
        letter = "D"
    else:
        letter = "F"
    print(letter)
    print()
    print()
    print('-'*14,'Results','-'*14)
    print("Lowest Score  :", lowest)
    print("Modified List :", grade_list)
    print("Scores Average:", format(ave, ',.2f'))
    print("Grade         :", letter)
    print('-'*45)
    choice = input('Would you like to run the program again? Enter yes or no: ')
print("Program has exited!")
    
    

