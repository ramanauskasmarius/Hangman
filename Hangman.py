from getpass import getpass
import string

def get_word():

    while True:

        word = getpass("Please enter a word to guess: ").upper()
        word2 = getpass("Please confirm a word: ").upper()

        check = any(chr.isdigit() for chr in word)

        if word == word2 and len(word.split()) < 2 and check == False:

            print('Word accepted. Lets play Hangman\n')
            break
        
        else:

            print("Your entered words doesnt match.\nYou must enter only 1 word.\nWord must be without any numbers.\nTry again.")
            continue

    return word

def game():

    while game:
    
        word = get_word()

        word_letters = set(word)

        used_letters = set()

        all_letters = set(string.ascii_uppercase)

        lives = 6

        while len(word_letters) > 0 and lives > 0:

            print("Your guessed letters: \n", ' '.join(used_letters))
            print(" ")

            hidden_word = [letter if letter in used_letters else '_' for letter in word]

            print("Your object: \n", ' '.join(hidden_word))

            user_guess = input("Guess a letter: \n").upper()

            if user_guess in all_letters - used_letters:
            
                used_letters.add(user_guess)

                if user_guess in word_letters:

                    word_letters.remove(user_guess)

                else:

                    lives -= 1
                    print(f"Entered letter not in a word.\nLives remaining: {lives}\n ")
        
            elif user_guess in used_letters:

                print("You tried this letter before. Try again.\n ")

            else:

                print("You entered a valid character.\n ")


        if lives == 0:
            
            print('Game over')
            print(f"You have 0 lives. The word was {word}")
            again = input("Want to play again? Y/N: ").upper()

        else:

            print(f"Congratulations, you won. The word was {word}")
            again = input("Want to play again? Y/N: ").upper()

        if again == 'Y':
            
            continue

        else:

            break


game()