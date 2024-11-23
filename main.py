import random


roll_count = 0

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        try:
            
            num_dice = int(input('How many dice you want to roll? '))
            
            if num_dice <= 0:
                print("please enter a number greater than 0.")
                continue

            rolls = [random.randint(1,6) for _ in range(num_dice)]
            print(f'You rolled: {rolls}')

            roll_count += 1
            print(f'total dice rolls: {roll_count}')

        except ValueError:
            print('Please enter a valid number for number of dices.')
    elif choice == 'n':
        print(f'Thanks for playing! you rolled the dice {roll_count} times in the current session')
        break
    else:
        print('Invalid choice!')
    