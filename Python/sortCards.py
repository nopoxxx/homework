def sortCards(cards):
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            if cards[j][0] < cards[i][0] or (
                cards[j][0] == cards[i][0] and cards[j][1] < cards[i][1]
            ):
                cards[i], cards[j] = cards[j], cards[i]
    return cards