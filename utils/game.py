import random

class Hangman:
    possible_words = ['becode', 'learning', 'mathematics', 'sessions'] # Creating a list of words to be guessed by the playey outside of methods 

    def __init__(self):
        
        
        self.word_to_find = list(random.choice(Hangman.possible_words))
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find) #Creating a list with a string _  in a  same length of word_to_find *multiplying it using len method.
        self.wrongly_guessed_letters = [] #Attribute that contains a list of strings where each element will be a letter guessed by the user that is not in the `word_to_find`
        self.lives = 5 #Max quantities  of tries in an another word 
        self.error_count = 0 #An error_count attribute that contains the number of errors made by the player.
        self.turn_count = 0 #A turn_count attribute that contain the number of turns played by the player. Might be omited 
        
                
            
    def play(self):

        """play() -> method that asks the player to enter a letter. Be careful that the player shouldn't be allowed to type something else than a letter, 
        and not more than a letter. If the player guessed a letter well, add it to the `correctly_guessed_letters` list. If not, add it 
        to the `wrongly_guessed_letters` list and add 1 to `error_count`"""

        while True:
            letter = input("U have to guess a word letter by letter, pls enter ur guess letter : ").lower()
            if letter.isdigit():
                print("only string are allowed")
                continue

            if letter in self.correctly_guessed_letters or letter in self.wrongly_guessed_letters:
                print(f"The letter {letter} is already proposed, please enter another letter ")
                continue

            elif letter in self.word_to_find:
                print(f"You guessed a Letter  {letter}")
                for i, char in enumerate(self.word_to_find):
                     if letter == char:
                          self.correctly_guessed_letters[i] = letter 
                #self.correctly_guessed_letters.append(letter)
                print(self.correctly_guessed_letters)
                self.turn_count += 1 

        
            else:
                self.error_count += 1
                print(f"You made {self.error_count} errors")
                self.lives -= 1
                print(f"You have {self.lives} left")

                print(f'The letter {letter} is not in the word')
                self.wrongly_guessed_letters.append(letter)
                print(self.wrongly_guessed_letters)


            if self.lives == 0:
                print("You lost the Game")
                break
            
            if self.correctly_guessed_letters == self.word_to_find:
                    print(f"You found the word: {self.word_to_find} in {self.turn_count}  with {self.error_count} errors!")
                    break
                
                
                



    # def game_over(self):

    #     """A `game_over()` method that will stop the game and print `game over...`.""" 
    #      #will call `game_over()` if `lives` is equal to 0.
        
       
    
            
        
    # def well_played(self):
        

    
    def start_game(self):
            self.play()
            
            """ A `start_game()` method that:
            - will call `play()` until the game is over (because the user guessed the word or because of a game over."""
            
        
        






