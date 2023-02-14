# Open a new text file for writing
with open('responses.txt', 'w') as file:

    # Ask the user for their name and write it to the file
    name = input('What is your name? ')
    file.write('Name: ' + name + '\n')

    # Ask the user for their age and write it to the file
    age = input('How old are you? ')
    file.write('Age: ' + age + '\n')

    # Ask the user for their favorite color and write it to the file
    color = input('What is your favorite color? ')
    file.write('Favorite Color: ' + color + '\n')

print('Thank you! Your responses have been recorded.')
