import card

games_til_shuffle = 10
game = card.Game()
game.start_game(True, 5)

while game.run_game():
    if games_til_shuffle < 1:
        games_til_shuffle = 10
        game.start_game(True, 5)
    else:
        game.start_game(False, 5)
