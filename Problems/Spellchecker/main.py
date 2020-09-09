dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
sentence = input()
bad_words = [word for word in sentence.split() if word not in dictionary]
if len(bad_words) > 0:
    for word in bad_words:
        print(word)
else:
    print('OK')
