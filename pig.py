import random
import argparse

def roll_die(sides=6):
    return random.randint(1, sides)

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.total_points = 0

    def display(self):
        print(f"{self.name} has {self.total_points} points.")

    def __str__(self) -> str:
        return f"{self.name} has {self.total_points} points."

    def play_turn(self):
        turn_points = 0
        while True:
            roll = roll_die()
            print(f"{self.name} rolled a {roll}")
            
            if roll == 1:
                print(f"{self.name} loses the turn! No points added.")
                turn_points = 0
                break
            else:
                turn_points += roll
                print(f"Current turn total for {self.name}: {turn_points}")

                decision = input("Roll again (r) or Hold (h)? ").lower()
                if decision == 'h':
                    self.total_points += turn_points
                    print(f"{self.name} holds with a total score of {self.total_points} points.")
                    break

    def reset(self):
        """Resets player's total points for new game."""
        self.total_points = 0

class Game:
    def __init__(self, players, win_points=100) -> None:
        self.players = players
        self.win_points = win_points
        self.winner = None

    def check_winner(self):
        for player in self.players:
            if player.total_points >= self.win_points:
                self.winner = player
                return True
        return False

    def play(self):
        current_player_idx = 0
        while not self.check_winner():
            current_player = self.players[current_player_idx]
            print(f"\nIt's {current_player.name}'s turn")
            current_player.play_turn()
            current_player_idx = (current_player_idx + 1) % len(self.players)
            print("----------------- End of Round ----------------")

        print(f"The winner is {self.winner.name}!")
        self.winner.display()

    def reset_game(self):
        """Resets the game for all players."""
        for player in self.players:
            player.reset()
        self.winner = None

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Pig Game")
    parser.add_argument('--numPlayers', type=int, default=2, help='Number of players (default is 2)')
    args = parser.parse_args()

    # Create players dynamically based on user input
    players = []
    for i in range(1, args.numPlayers + 1):
        player_name = input(f"Enter name for Player {i}: ")
        players.append(Player(player_name))

    game = Game(players)

    while True:
        game.play()
        
        play_again = input("\nWould you like to play another game? (y/n): ").lower()
        if play_again == 'y':
            game.reset_game()  # Reset game state for a new round
        else:
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()


    
