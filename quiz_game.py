
# Now let's add a timer to the quiz game. We'll use the time module to do this.
# We'll start by importing the time module at the top of the file.
# Then we'll create a variable called start_time and set it equal to time.time().
# This will store the time when the game starts.
# Then we'll create a variable called end_time and set it equal to time.time().
# This will store the time when the game ends.
# Then we'll create a variable called time_taken and set it equal to end_time minus start_time.
# This will give us the time taken to complete the quiz.
# Then we'll print out the time taken to complete the quiz.
# We'll also add a timer to each question.
# We'll start by creating a variable called start_time and set it equal to time.time().
# This will store the time when the question starts.
# Then we'll create a variable called end_time and set it equal to time.time().
# This will store the time when the question ends.
# Then we'll create a variable called time_taken and set it equal to end_time minus start_time.

# Path: quiz_game.py

import time

print('Welcome to the Quiz Game!')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print('Okay! Let\'s play!')
time.sleep(1)

score = 0

# create switch for questions and answers
answer = input('What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('Correct!')
    score += 1

else:
    print('Incorrect!')

time.sleep(1)

answer = input('What does GPU stand for? ')

if answer.lower() == 'graphics processing unit':

    print('Correct!')
    score += 1

else:

    print('Incorrect!')

time.sleep(1)

answer = input('What does RAM stand for? ')

if answer.lower() == 'random access memory':

    print('Correct!')
    score += 1

else:

    print('Incorrect!')

time.sleep(1)

answer = input('What does PSU stand for? ')

if answer.lower() == 'power supply unit':

    print('Correct!')
    score += 1

else:

    print('Incorrect!')

time.sleep(1)

answer = input('What does HDD stand for? ')

if answer.lower() == 'hard disk drive':

    print('Correct!')
    score += 1

else:

    print('Incorrect!')

time.sleep(1)

answer = input('What does SSD stand for? ')

if answer.lower() == 'solid state drive':

    print('Correct!')
    score += 1

else:

    print('Incorrect!')

time.sleep(1)

answer = input('What does VRAM stand for? ')

if answer.lower() == 'video random access memory':

    print('Correct!')
    score += 1

else:

    print('Incorrect!')

time.sleep(1)

answer = input('What does BIOS stand for? ')

if answer.lower() == 'basic input output system':

    print('Correct!')
    score += 1

else:

    print('Incorrect!')

time.sleep(1)

answer = input('What does UEFI stand for? ')

if answer.lower() == 'unified extensible firmware interface':

    print('Correct!')
    score += 1

else:

    print('Incorrect!')

time.sleep(1)

answer = input('What does VRM stand for? ')

if answer.lower() == 'voltage regulator module':

    print('Correct!')
    score += 1

else:

    print('Incorrect!')

time.sleep(1)

# print final score

print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score / 10) * 100) + '%.')

# print time taken to complete quiz

start_time = time.time()
end_time = time.time()
time_taken = end_time - start_time
print('You took ' + str(time_taken) + ' seconds to complete the quiz.')
