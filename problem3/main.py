def playing_domino(cards, deck):

    valid_cards = [card for card in cards if deck[0] in card or deck[1] in card]

    if not valid_cards:
        return []

    def card_sum(card):
        return sum(card)

    return max(valid_cards, key=card_sum)

if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []