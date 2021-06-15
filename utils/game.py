
#import randomness and list of word

import random
from word_list import possible_words

#create class hangman with multiple methods : start_game, play_game, game_over
#define word_to_find, lives, turns, errors & correctly_guessed_letters
#return word_to_find in uppercase for ease of use

class Hangman:
    def __init__(self):

        self.word_to_find = random.choice(possible_words)
        self.lives = 5
        self.well_guessed_letters = []
        self.word_to_complete = "_" * len(self.word_to_find)
        self.length_word_to_find = len(self.word_to_find)
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
        self.word_to_find.upper()
        self.guessed = False

#Init methods
        self.start_game(self.lives, self.guessed)
        self.play_game()

#this method calls the play_game(), well_played(), game_over()
    def start_game(self, lives, guessed):
        if guessed is False and lives > 0:
            self.play_game()
        if guessed :
            self.well_played()
        if lives == 0:
            self.game_over()
        print("\nStatus: these letters have been found: ", self.well_guessed_letters," these are your mistakes: ", self.wrongly_guessed_letters)
        print("You have this many lives left: ", lives, "You've made this many mistakes: ",self.error_count, "and guessed this many times: ",self.turn_count)

#this method is called when the player doesn't have any lives left and asks if players wants to play again.
    def game_over(self):
        if self.lives == 0:
            print("Game Over, you ran out of lives. The word was " + self.word_to_find + ". Maybe next time?")
            self.try_again = input("Do You want to play, again ?").upper()
            if self.try_again == "Y":
                self.play_game()
            else:
                exit()

#this method is called when the player guessed the word_to_find

    def well_played(self):
        print(" Good Job, Buddy! you've found the word", self.word_to_find, "in ", self.lives, "with" ,self.well_guessed_letters, "you only had this many errors", self.error_count, "and you did it in this many turns", self.turn_count  )
        self.try_again = input("Do You want to play, again ?").upper()
        if self.try_again == "Y":
            self.play_game()
        else:
            exit()
#this method is the game play. displaying the word_to_find, guessing and completing the word_to_find and calling the print function of start_game()

    def play_game(self): #, word_to_find):
        # COACHES' NOTE: this method is waaay too long. subdivide into smaller functions like 'inform_user', 'update_game_state',....
        guessed = False
        print("\n")
        # COACHES' NOTE: You should not use comments to compensate for a lack of functions. They just make the project seem more cluttered.
#We help the player by giving the length of word

        print(self.word_to_complete," ", "the length of the word is : ", self.length_word_to_find)
        print("\n")

#As long the world hasn't been found
        while not guessed and self.lives > 0:
            guess = input("\nPlease enter a letter: ").upper()

#if the guess is a letter and is part of the alphabet: add to well_guessed_letters list

            if len(guess) == 1 and guess.isalpha():

#if already guessed, the player add to his turn and error count

                if guess in self.well_guessed_letters:
                    print("You have already guessed this letter")
                    self.turn_count += 1
                    self.error_count += 1
                    print("\n")
                    print(self.word_to_complete," ", "the length of the word is : ", self.length_word_to_find)
                    print("\n")
                    print("Status: these letters have been found: ", self.well_guessed_letters," these are your mistakes: ", self.wrongly_guessed_letters)
                    print("You have this many lives left: ", self.lives, "You've made this many mistakes: ",self.error_count, "and guessed this many times: ", self.turn_count)
                    #self.start_game()

#if the guess is not in the word_to_find, players loses a life and adds a turn and error count
                elif guess not in self.word_to_find :
                    print(guess, "is not in word")
                    self.lives -= 1
                    self.turn_count += 1
                    self.error_count += 1
                    self.wrongly_guessed_letters.append(guess)
                    print("\n")
                    print(self.word_to_complete," ", "the length of the word is : ", self.length_word_to_find)
                    print("\n")
                    #self.start_game(self.lives, guessed)
                    print("Status: these letters have been found: ", self.well_guessed_letters," these are your mistakes: ", self.wrongly_guessed_letters)
                    print("You have this many lives left: ", self.lives, "You've made this many mistakes: ",self.error_count, "and guessed this many times: ", self.turn_count)

#if guess is a letter in word, add count, add guess to well guessed_letters list
                else :
                    print("Woohoo", guess, "is correct!")
                    self.turn_count += 1
                    self.well_guessed_letters.append(guess)
                    self.word_to_complete_as_list = list(self.word_to_complete)

#we iterate trought new list (word_to_complete_as_list) to match the index of the (word_to_find) and the guess the user has input and return found letters in word_to_complete

                    indexes = [index_word for index_word, letter in enumerate(self.word_to_find) if letter == guess]
                    for index in indexes:
                        self.word_to_complete_as_list[index] = guess
                    word_to_complete = "".join(self.word_to_complete_as_list)
                    print("\n")
                    print(word_to_complete," ", "the length of the word is : ", self.length_word_to_find)
                    print("\n")
                    #self.start_game(self.lives, guessed)
                    print("Status: these letters have been found: ", self.well_guessed_letters," these are your mistakes: ", self.wrongly_guessed_letters)
                    print("You have this many lives left: ", self.lives, "You've made this many mistakes: ",self.error_count, "and guessed this many times: ", self.turn_count)

# if there's no more letters unknown ("_") the user has guessed right and we call up the well_played()
                    if "_" not in word_to_complete:
                        Guessed = True
                        self.well_played()

# Error message if user uses an invalid char or doesn't input a letter

            elif len(guess) > 1:
                print("You can only guess A letter")
                self.turn_count += 1
                self.error_count += 1
                self.wrongly_guessed_letters.append(guess)
                print("\n")
                print(self.word_to_complete ," ", "the length of the word is : ", self.length_word_to_find)
                print("\n")
                #self.start_game(self.lives, guessed)
                print("Status: these letters have been found: ", self.well_guessed_letters," these are your mistakes: ", self.wrongly_guessed_letters)
                print("You have this many lives left: ", self.lives, "You've made this many mistakes: ",self.error_count, "and guessed this many times: ", self.turn_count)
            else :
                print("Not a valid guess")
                print("\n")
                #self.start_game(self.lives, guessed)
                print("Status: these letters have been found: ", self.well_guessed_letters," these are your mistakes: ", self.wrongly_guessed_letters)
                print("You have this many lives left: ", self.lives, "You've made this many mistakes: ",self.error_count, "and guessed this many times: ", self.turn_count)
                return self.word_to_find
        print("\n")
        print(self.word_to_complete ," ", self.length_word_to_find)
        print("\n")
        #self.start_game(self.lives,self.guessed)
        print("Status: these letters have been found: ", self.well_guessed_letters," these are your mistakes: ", self.wrongly_guessed_letters)
        print("You have this many lives left: ", self.lives, "You've made this many mistakes: ",self.error_count, "and guessed this many times: ", self.turn_count)

        if guessed:
            self.well_played()
        else:
            self.game_over()

if __name__ == "__main__":
    Hangman()

# COACHES' NOTE: Decent, but too many comments that could have been functions. Don't go on a comment free spree, only use them when absolutely needed.
    
  
