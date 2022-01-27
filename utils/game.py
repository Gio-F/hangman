
class Hangman:
    """Class containing the attributes
    needed to play the game.
    1.pick a word in the possible_words list
    2.create a list of _ as long as the word 
    3.ask user to guess a letter
    4.if guess respects rules, count one turn
    4.if guess is right, change "_"
    5.start again from 3
    6.if guess is wrong, add letter to wrongly_guessed_letters
    7.start again from 3
    """

    def __init__(self):
        
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = ["b","e","c","o","d","e"]
        self.correctly_guessed_letters = [" _ ", " _ "," _ "," _ "," _ "," _ "]          
        self.lives = 5
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
        print(self.possible_words, self.word_to_find,self.correctly_guessed_letters,self.lives)

        
    def play(self):
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
        if self.guess not in self.word_to_find:
            self.error_count += 1
            self.lives -= 1
            self.wrongly_guessed_letters.append(self.guess)
            print(f"Wrong! Here your wrong guesses{self.wrongly_guessed_letters}")
                    
        
        if self.guess in self.word_to_find:
            for i, letter in enumerate(self.word_to_find):
                if letter == self.guess:
                    self.correctly_guessed_letters[i] = self.guess
            print(self.correctly_guessed_letters)

        return

    def well_played(self):
        if self.word_to_find == self.correctly_guessed_letters:
            print (f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")

    def game_over(self):
        print("game over...")

    def start_game(self):
        
        while self.lives > 0 and self.correctly_guessed_letters != self.word_to_find:
            self.play()
        if self.lives <= 0:
            self.game_over()
        if self.word_to_find == self.correctly_guessed_letters:
            self.well_played()
            
        return

    


hangman = Hangman()  
hangman.start_game()


       