
class Hangman:
    """Class containing the attributes
    needed to play the game.
    : self.possible_words: list of strings from which 
    one will be randomly chosen from a list
    : self.word_to_find: list of strings created from
    each element of the previously selected string
    : self.correctly_guessed_letters: list of strings, at the 
    start each element correspond to a blank to fill in format " _ "
    : self.lives: int used to limit the number of turns
    when more than 5 errors are made
    : self.wrongly_guessed_letters: list of strings, at the start empty,
    then appended with user's input not matching the word_to_find
    : self.turn_count: int that is incremented by 1 
    when valid user's input is provided
    : self.error_count: int that is incremented by 1 
    when user's input not matching the word_to_find
    """

    def __init__(self):
        
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = ["b","e","c","o","d","e"]
        self.correctly_guessed_letters = [" _ ", " _ "," _ "," _ "," _ "," _ "]          
        self.lives = 5
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
        

        
    def play(self):
        """ Method that asks the user to input one letter and
        checks that the input is a lower case letter and it is only one
        characters. 
        When the input is valid, it increases self.turn_count by 1.
        """

        import string
        valid_input =[]
        self.guess = str(input("Please enter a letter: "))
        if self.guess not in string.ascii_lowercase:
           print ('Please enter only lowercase letters')
        if len(self.guess) != 1:
              print ('Please enter only one character')
        else:
            valid_input.append(self.guess)

        self.turn_count += 1
        print(f"You played {self.turn_count} turns")

        """ If the valid input is a wrong guess, self.error_count is incremented by 1
         and self.lives is decreased by 1. 
         The input is appended to the list wrongly_guessed_letters
         """
        if self.guess not in self.word_to_find:
            self.error_count += 1
            self.lives -= 1
            self.wrongly_guessed_letters.append(self.guess)
            print(f"Wrong! Here your wrong guesses{self.wrongly_guessed_letters}")

        """ If the valid input is a right guess, we retrieve the index 
        of the correctly guessed letter (using enumerate to iterate in case
        of more instances). Using the index as reference, we substitute the 
        blank at the same index in self.correctly_guessed_letters with the 
        guessed letter
         """            
        
        if self.guess in self.word_to_find:
            for i, letter in enumerate(self.word_to_find):
                if letter == self.guess:
                    self.correctly_guessed_letters[i] = self.guess
            print(self.correctly_guessed_letters)

        return

    def well_played(self):
        """ Method that will print a message when the word is correctly guessed"""
        if self.word_to_find == self.correctly_guessed_letters:
            print (f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")

    def game_over(self):
        """ Method that will print a message when all lives have been used"""
        print("game over...")

    def start_game(self):
         """ Method that will start the game when called, and runs it by
         calling the previously defined methods in the class"""
        
         while self.lives > 0 and self.correctly_guessed_letters != self.word_to_find:
            self.play()
         if self.lives <= 0:
            self.game_over()
         if self.word_to_find == self.correctly_guessed_letters:
            self.well_played()
            
         return

    
hangman = Hangman()  
hangman.start_game()


       