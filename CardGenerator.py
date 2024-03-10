"""Card Generator for Skyjo"""

import random
random.seed = 1


class CardGenerator():
    def __init__(self) -> None:
        self.number_range = []
        negative_range = [-2, -1]
        for neg in negative_range:
            self.number_range.extend([neg for _ in range(5)])
        self.number_range.extend([0 for _ in range(15)])
        positive_range = [x for x in range(1, 13)]
        for pos in positive_range:
            self.number_range.extend([pos for _ in range(10)])
        # print(self.number_range)

    def get_card(self):

        return self.number_range[random.randint(0, len(self.number_range))]


if __name__ == "__main__":
    cg = CardGenerator()
    print(cg.get_card())
