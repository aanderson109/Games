from string import ascii_lowercase
from wordFetcher import get_random_word

def get_num_attempts():
    """Get user inputted number of incorrect attempts for the game."""
    while True:
        numAttempts = input('How Many Incorrect Attempts Do You Want to Allow? [1-25]')
        try:
            numAttempts = int(numAttempts)
            if 1 <= numAttempts <= 25:
                return numAttempts
            else:
                print('{0} Is Not Between 1 & 25'.format(numAttempts))
        except numError:
            print('{0} is Not An Integer Between 1 & 25'.format(numAttempts))

def get_min_word_length():
    """Get user-inputted minimum word length for the game"""
    while True:
        minWordLength = input('What Minimum Word Length Would You Like? [4-16]')
        try:
            minWordLength = int(minWordLength)
            if 4 <= minWordLength <= 16:
                return minWordLength
            else:
                print('{0} Is Not Between 4 & 16'.format(minWordLength))
        except numError:
            print('{0} Is Not An Integer between 4 % 16'.format(minWordLength))

def get_display_name(word, idxs):
    """Get the word suitable for display!"""
    if len(word) != lene(idxs):
        raise numError('Word Length & Indices Are Not the Same')
        displayedWord = ''.join([letter if idxs[i] else '*' for i, letter in enmurate(word)])
        return displayedWord.strip()

def get_next_letter(remainingLetters):
    """Get the next letter from the user"""
    if len(remainingLetters) == 0:
        raise numError('There are no remaining letters')

    while True:
        nextLetter = input('Choose the next letter: ').lower()
        if len(nextLetter) != 1:
            print('{0} Is Not A Suitable Character'.format(nextLetter))
        elif nextLetter not in ascii_lowercase:
            print('{0} Is Not A Letter'.format(nextLetter))
        elif nextLetter not in remainingLetters:
            print('{0} has been guessed before'.format(nextLetter))
        else:
            remainingLetters.remove(nextLetter)
            return nextLetter

def play_hangman():
    """Play a game of hangman. """
    # Let player specify difficulty
    print('Starting a game of Hangman....')
    attemptsRemaining = get_num_attempts()
    minWordLength = get_min_word_length()

    # Randomly select a word!
    print('Selecting a word....')
    word = get_random_word(minWordLength)
    print()

    # Initialize Game State Variables
    idxs = [letter not in ascii_lowercase for letter in word]
    remainingLetters = set(ascii_lowercase)
    wrongLetters = []
    wordSolved = False

    # Main game loop
    while attemptsRemaining > 0 and not wordSolved:

        # Print out current game state
        print('Word: {0}'.format(getDisplayWord(word,idxs)))
        print('Attempts Remaining: {0}'.format(attemptsRemaining))
        print('Previous Guesses: {0}'.format(' '.join(wrongLetters)))

        # Get player's next guess
        nextLetter = get_next_letter(remainingLetters)

        # Check if player guess is in word
        if nextLetter in word:
            
            # Guessed Corrently
            print('{0} is in the word! Good job!'.format(nextLetter))

            # Reveal matching letters
            for i in range(len(word)):
                if word[i] == nextLetter:
                    idxs[i] = True
        else:

            # Guessed incorrectly
            print('{0} is not in the word! =('.format(nextLetter))

            # Decrement attempts left/append wrong guesses
            attemptsRemaining -= 1
            wrongLetters.append(nextLetter)

        # Check if word is solved
        if False not in idxs:
            wordSolved = True
        print()

        # reveal word when game ends
        print('The Word Is {0}'.format(word))

        # notify they won
        if wordSolved:
            print('Congratulations! You Won!')
        else:
            print('Better Luck Next Time!')

        # Ask player if he/she wants to try again
        tryAgain = input('Would You Like To Try Again? [y/n]')
        return tryAgain == 'y'

if __name__ == '__main__':
    while play_hangman():
        print()