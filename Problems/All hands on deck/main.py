cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
my_cards = 0
for _i in range(6):
    my_cards += cards[input()]
print(my_cards / 6)
