#Matthew Howe
#4/23/24
#P4HW2
#Calculate every employee's pay, overtime, and hours

totOvertime = 0
totRegPay = 0
totGrossPay = 0
count = 0
employee = input("Enter employee's" + ' name or "Done" to terminate: ')
while employee != "Done":
    hrs = float(input("Enter the number of hours worked this week: "))
    rate = float(input("Enter the employee's pay rate: "))
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
    totOvertime = totOvertime + ovtp
    totRegPay = totRegPay + rpay
    totGrossPay = totGrossPay + gpay
    count = count + 1
    print('-'*37)
    print("Employee name: "+ employee)
    print()
    print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
    print('-'*80)
    print(f'{hrs:<16.1f}{rate:<12.1f}{ovth:<12.1f}{ovtp:<16.2f}${rpay:<15.2f}${gpay:<10.2f}')
    employee = input("Enter employee's" + ' name or "Done" to terminate: ')
print("Total number of employee's entered: " + str(count))
print("Total amount paid for overtime: $" + str(format(totOvertime,'.2f')))
print("Total amount paid for regular hours: $" + str(format(totRegPay,'.2f')))
print("Total amound paid in gross: $" + str(format(totGrossPay,'.2f')))
print("Program has exited")

#Create accumulators for totaling up employee count, gross pay, overtime par, and regular pay
#Create while loop for a repeating program with an exit prompt
#Print all accumulator values after the program is terminated
