import random

def myshuffle(cards):

    for i in range(1,52):

        temp = random.randint(0,i) # randint inkluderar ju båda gränserna
        cards[i],cards[temp] = cards[temp],cards[i]

def cardshuffle():
    cards = []
    for i in range(0,52): # korten lagras i listan i positionerna 0..51
        cards.append(i % 13) # kortens valörer representeras som 0..12

    myshuffle(cards)
    return cards
