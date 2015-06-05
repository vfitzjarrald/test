import random
from random import randint

def main():
    print '>> New game started.\n>> Good luck!\n'
    answer = generateAnswer()
    while True:
        userGuess = getUserGuess()
        if userGuess == answer:
            print '>> Congratulations, you won!'
            return
        print '>> The answer you provided is incorrect.\n>> Perhaps this hint will help you: '
        giveFeedback(answer, userGuess)

def generateAnswer():
    answer = ''
    for i in range(4):
        digit = str(randint(0,9))
        answer += digit
    return answer

def getUserGuess():
    while True:
        guess = raw_input('>> Please enter a 4-digit number: ').strip()
        return guess

def giveFeedback(answer, guess):
    for i in range(4):
        if guess[i] == answer[i]:
            print 'X',
            continue
        if guess[i] in answer:
            print 'O',
            continue
        print '-',
    print '\n'

if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        print '>> Fatal error: %s' % e