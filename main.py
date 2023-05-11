from utils.game import Hangman


while True:
    game = Hangman()
    game.start_game()

    # Asking whetere a user wants to play again or not 
    if input("Wanna play again? ").lower() != 'y':
        break
    
