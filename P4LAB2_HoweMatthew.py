num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num2 < num1:
    print("Second integer can't be less than the first.")
else:
    for i in range(num1,num2 + 1, 5):
        print(f'{str(i)}', end=' ')
    print()