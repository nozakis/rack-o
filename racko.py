import names
from player import Player
from deck import Deck


def main():
    # Get player count
    player_count = int(input('How many players? '))
    players = []

    # Assign names
    for i in range(player_count):
        name = input(f'Enter name for player {i + 1} or leave blank for a random name:\n')
        if len(name) == 0:
            name = names.get_first_name()

        player = Player(name)
        players.append(player)

    round_num = 0
    # Round loop
    while True:
        for player in players:
            player.rack = []

        player_index = round_num % player_count
        print(f'Round {round_num + 1}! {players[player_index].name} goes first.')
        deck = Deck()
        deck.deal(players)

        # Turn loop plays and checks if the playing player has fRacked-Em-Up-O
        player = players[player_index]
        while not player.play(deck):
            input(f'{player.name}\'s turn is over. Press Enter to continue.\n')
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            player_index += 1
            player = players[player_index % player_count]
            input(f'{player.name} is next up! Press Enter to continue.\n')

        print(f'{player.name} has fRacked-Em-Up-O! ┌(・。・)┘♪ ♪┏(・o･)┛♪')

        # Score players after a player has fRacked-Em-Up-O
        # add players with a score over the winning amount to winners
        winners = []
        for player in players:
            player.game_score += player.round_score
            if player.game_score >= 150:
                winners.append(player)

        # Print player scores after round before
        # checking for final name winner
        print(f'Scores for Round {round_num + 1}:')
        for player in players:
            print(f'{player.name}: {player.game_score}')

        # determine which player with a score over the winning amount has
        # the highest score and announce their victory
        if len(winners) != 0:
            max_score = 0
            winner = None
            for player in winners:
                # TODO: deal with edge case of tie winners
                if player.game_score > max_score:
                    max_score = player.game_score
                    winner = player
            print(f'{winner.name} has won!')
            # TODO: Maybe winning ascii art?? also ask
            # the player if they want to play another round and restart program
            return

        round_num += 1
        input(f'Press Enter key to start round {round_num + 1}')


def print_ascii_crap():
    print('')  # TODO


if __name__ == '__main__':
    main()
