import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            return 0

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def count_vowels(self, word: str):
        vowels = "aeiouAEIOU"
        return sum(1 for char in word if char in vowels)

    def round_winner(self, player1_word: str, player2_word: str):
        count1 = self.count_vowels(player1_word)
        count2 = self.count_vowels(player2_word)

        if count1 > count2:
            return 1
        elif count2 > count1:
            return 2
        else:
            return 0

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        input = {"rock", "paper", "scissors"}

        if player1_word not in input and player2_word not in input:
            return 0

        if player1_word not in input:
            return 2

        if player2_word not in input:
            return 1

        if player1_word == player2_word:
            return 0

        if (player1_word == "rock" and player2_word == "scissors") or \
            (player1_word == "paper" and player2_word == "rock") or \
            (player1_word == "scissors" and player2_word == "paper"):
            return 1
        else:
            return 2
