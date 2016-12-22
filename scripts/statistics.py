import json
from pymystem3 import Mystem


def get_numbers(file_name):
    with open('{}.json'.format(file_name), 'r', encoding='utf-8') as f:
        tweets = json.load(f)

    for i, tweet in enumerate(tweets, start=1):
        print(tweet['text'])

    print('Total: {}'.format(len(tweets)))


def get_argument(m, file_name):
    with open('{}.json'.format(file_name), 'r', encoding='utf-8') as f:
        tweets = json.load(f)

    neg = 0

    with open('{}.csv'.format(file_name), 'w', encoding='utf-8') as w:

        for i, tweet in enumerate(tweets, start=1):
            # if i == 64:
            #     break
            w.write('{}\t\t\t\t{}\n'.format(
                tweet['text'].replace('\n', ' '),
                '1sg'
            ))
            # tokens = tweet['text'].lower().split()
            # if 'не умею' in tweet['text'].lower():
            #     neg += 1
            #     continue
            # if 'не' in tokens:
            #     print(tokens)
            #     neg += 1
            #     continue

    print(neg)
            # print(tweet['text'])
            # print('\n=====\n')
    #     tokens = m.lemmatize(tweet['text'])
    #     # print(tokens)
    #     for j, token in enumerate(tokens):
    #         if token == 'уметь':
    #             # print('foo')
    #             print(tokens[j+4])
    #
    # print('Total: {}'.format(len(tweets)))


def main():
    m = Mystem()
    # get_numbers('умеем_в_cleared')
    get_argument(m, 'умею')


if __name__ == '__main__':
    main()
