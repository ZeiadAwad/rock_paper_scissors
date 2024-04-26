
def welcome_message():
    print("============ Welcome to Our Game ============")
    print("========== Rock , Paper , Scissors ============")


def play_again():
    yes_or_no = ["y", "n"]

    want_to_play_again = None
    while want_to_play_again not in yes_or_no:
        want_to_play_again = input("Want to play again y / n ? ").lower()

    if want_to_play_again == 'y':
        return True
    else:
        return False
