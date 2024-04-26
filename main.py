import game
import utiles


utiles.welcome_message()
want_to_play = True

while want_to_play:
    game.start()
    want_to_play = utiles.play_again()

