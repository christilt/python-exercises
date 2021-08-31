# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9

        self._guesses = set()
        self._word = word

    def guess(self, char):
        if (self.get_status() != STATUS_ONGOING):
            raise ValueError("game over")

        if (char in self._word and
            char not in self._guesses):
                self._guesses.add(char)
        else:
            self.remaining_guesses -= 1

    def get_masked_word(self):
        return "".join(
            x if x in self._guesses else "_"
            for x in self._word
        )

    def get_status(self):
        if ("_" not in self.get_masked_word()):
            return STATUS_WIN
        elif (self.remaining_guesses >= 0):
            return STATUS_ONGOING
        else:
            return STATUS_LOSE
