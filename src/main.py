""" Athor: Bouji-dev
        Date created: 12/22/2024
        Description: Rock paper scissors game.
"""

import random
from typing import List, Tuple

class RockPaperScissors:
    def __init__(self, name: str):
        """main class for Rock paper scissors game"""
        self.choices: List[str] = ['rock', 'paper', 'scissors']
        self.player_name = name

    def get_player_choice(self):
        user_choice: str = input(f"Enter your choice {self.choices} :")
        if user_choice.lower() in self.choices:
            return user_choice.lower()

        print(f"Invalid choice. you must select from {self.choices}.")    
        return self.get_player_choice()
    
    def get_computer_choice(self):
        """provide choice for machine randomly.
        :return: random choice from choices
        :rtype: str
        """
        return random.choice(self.choices)

    def decide_winner(self, user_choice: str , computer_choice: str) -> str:
        """ print winner based on user and computer choices

        :param user_choice: the choice of user
        :param computer_choice: the choice of  computer
        :return: print the winner
        :rtype: _str_
        """
        if user_choice == computer_choice:
            return "It's a Tie!"
        win_combinations: List[Tuple[str, str]] = [('rock, scissors'), ('paper', 'rock'), ('scissors', 'paper')]
        for win_comb in win_combinations:
            if (user_choice == win_comb[0]) & (computer_choice == win_comb[1]):
                return "Congeratulations! You won!"
            
        return "Oh no! The computer won!"
        
    def play(self):
        """ play the game.
        - get user choice.
        - get computer choice.
        - decide and print the winner.
        """
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()    
        winner_msg = self.decide_winner(user_choice, computer_choice)
        print(f"computer choice is {computer_choice}")
        print(winner_msg)


if __name__ == '__main__':
    game = RockPaperScissors('Ehsan')

    
while True:
    game.play()

    continue_game = input('Do you want to play again? (Enter any to play again or Enter q/Q to exit.)')    
    if continue_game.lower() == 'q':
        break