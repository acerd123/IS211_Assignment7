import random


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

class Game:
    def __init__ (self, player1, player2, win_points = 100 ) -> None:
        self.players = [player1, Player2]
        self.win_points - win_points
        self.winner = None

    def check_winner(self):
        for player in self.players:
            if player.total_points >= self.win_points:
                self.winner = Player
                return True
            
        return False


    def play(self):
        
        current_player_idx = 0
        while not self.check_winner():
            current_player = self.players[current_player_idx]
            print(f"It's {current_player,name}'s Turn")

            current_player.play_turn() 


            current_player_idx = 0 if current_player_idx == 1 else 1
            print("----------------- End of Round ----------------")


        print(f"The winner is {self.winner.name}")
        self.winner.display()



if __name__ == "__main__":
    p1 = Player("Alice")
    p2 = Player("Bob")

    p1.display()
    p2.display()

    
