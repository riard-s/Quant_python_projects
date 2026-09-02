import random


def build_deck():
    deck = []
    for rank in range(1, 14):  # ace=1, 2-10 as normal, jack=11, queen=12, king=13
        for suit in range(4):
            deck.append(rank)
    return deck


theo_ev = sum(build_deck()) / len(build_deck())
print(f"theoretical EV of card draw is: {theo_ev}")

num_hands = 1000000
hand_size = 5
total = 0

for i in range(num_hands):
    deck = build_deck()
    random.shuffle(deck)
    hand = deck[:hand_size]
    total += sum(hand)

average_card_value = total / (num_hands * hand_size)
print(
    f"Average card value across {num_hands} hands of {hand_size}: {average_card_value}")
