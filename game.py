import random


class Game:
    source_number = None
    number_size = None
    alphabet = list(range(10))

    attempts = []

    def generate_number(self):
        self.source_number = ""
        random.shuffle(self.alphabet)
        for i in range(self.number_size):
            self.source_number += str(self.alphabet[i])

    def guess(self, attempt):
        bools_and_cows = [0, 0]
        for i in range(self.number_size):
            index_of_coincidence = self.source_number.find(attempt[i])
            if index_of_coincidence != -1:
                bools_and_cows[0 if index_of_coincidence == i else 1] += 1
        self.attempts.append([attempt, bools_and_cows])
        return bools_and_cows

    def start(self, number_size):
        self.number_size = int(number_size)
        self.attempts = []
        self.generate_number()

