#Matthew Howe
#3/26/24
#P3HW2

employee = input("Enter employee's name: ")
hrs = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))

if hrs > 40:
    rpay = rate * 40
    ovth = hrs - 40
    ovtr = 1.5 * rate
    ovtp = ovth * ovtr
    gpay = rpay + ovtp
else:
    ovth = 0
    ovtp = 0
    rpay = rate * hrs
    gpay = rpay + ovtp
    

print('-'*37)
print("Employee name:   "+ employee)
print()
print("Hours Worked   Pay Rate    OverTime    OverTime Pay        RegHour Pay         Gross Pay")
print('-'*95)
print(f'{hrs:<15.1f}{rate:<12.1f}{ovth:<12.1f}{ovtp:<20.2f}${rpay:<20.2f}${gpay:<10.2f}')
