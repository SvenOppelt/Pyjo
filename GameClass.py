"""Game Class"""
import random
import numpy as np
import time

from CardGenerator import CardGenerator


def print_function_name(func, *args, **kwargs):
    def inner():
        func(*args, **kwargs)
        print(func.__name__)
    return inner


class Game():
    def __init__(self, id) -> None:
        self.id = id
        self.cg = CardGenerator()
        self.visible_cards = np.full((3, 4), False)
        cards = np.empty(12)
        for idx in range(12):
            cards[idx] = self.cg.get_card()
        self.cards = cards.reshape(3, 4)
        for _ in range(2):
            row = random.randint(0, 2)
            column = random.randint(0, 3)
            self.visible_cards[row, column] = True
        self.stack = self.cg.get_card()
        self.moves = 0

    def get_sum(self):
        return self.cards.sum()

    def play(self, rounds):

        while not self.game_finished():
            self.print_game()
            print("next round")
            self.game_logic()
            self.moves += 1
            time.sleep(1)
            if self.moves > rounds:
                break
        print()
        print("_________________Game is finished________________")
        self.print_game()

    def game_finished(self):
        if np.any(self.visible_cards):
            return False

        return True

    def game_logic(self):
        visible = self.cards*self.visible_cards
        high_value = visible.max()
        high_index_row = np.argmax(visible, axis=1)[0]
        high_index_col = np.argmax(visible, axis=0)[0]
        if self.stack < high_value:
            self.use_stack_card(high_index_row, high_index_col)
        else:
            draw_card = self.cg.get_card()
            if high_value < draw_card:
                self.draw_card_fold(draw_card, 2, 2)
            else:
                self.draw_card_use(draw_card, high_index_row, high_index_col)

    def use_stack_card(self, row, column):
        print("use stack card")
        self.cards[row, column], self.stack = self.stack, self.cards[row, column]
        self.visible_cards[row, column] = True

    def draw_card_fold(self, draw_card, row, column):
        print("draw card fold")
        self.stack = draw_card
        self.visible_cards[row, column] = True

    def draw_card_use(self, draw_card, row, column):

        print("draw card use")
        self.stack = self.cards[row, column]
        self.cards[row, column] = draw_card
        self.visible_cards[row, column] = True

    def print_game(self):
        print(f"__________ Game {self.id}________________")
        print(self.cards * self.visible_cards)
        print(f"{self.stack=}")
        print(f"{self.get_sum() = }")
        print(f"{self.moves = }")
        print()


if __name__ == "__main__":
    game = Game(0)
    game.play(20)
