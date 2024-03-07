#Matthew Howe
#3/5/24
#P2HW2
#Creating a list for grade input and calculations



my_list = []

x = float(input("Enter grade for Module 1: "))

my_list.append(x)

x = float(input("Enter grade for Module 2: "))

my_list.append(x)

x = float(input("Enter grade for Module 3: "))

my_list.append(x)

x = float(input("Enter grade for Module 4: "))

my_list.append(x)

x = float(input("Enter grade for Module 5: "))

my_list.append(x)

x = float(input("Enter grade for Module 6: "))

my_list.append(x)

length = len(my_list)

lowest = min(my_list)

highest = max(my_list)

total = sum(my_list)

ave = total/length

print()

print("------------Results------------")

print("Lowest Grade:".ljust(20) + str(format(lowest,'.1f')))

print("Highest Grade:".ljust(20) + str(format(highest,'.1f')))

print("Sum of Grades:".ljust(20) + str(format(total,'.1f')))

print("Average:".ljust(20) + str(format(ave,'.2f')))

print('-' *31)

##Create list
##Input floats as input tabs to allow grade entry
##Tag each as append(x)
##Create length tag
##Create lowest grade tag
##Create highest grade tag
##Create total tag
##Create average tag
##Print lowest with justification as string
##Print highest with justification as string
##Print total with justification as string
##Print average with justification as string
