import json


def clear(file_name):
    cleared_tweets = []
    with open('{}.json'.format(file_name), 'r', encoding='utf-8') as f:
        tweets = json.load(f)

    for i, tweet in enumerate(tweets, start=1):
        print(tweet['text'])

        allowed = input('{}: '.format(i))
        if allowed:
            cleared_tweets.append(tweet)

    print('Cleared: {}'.format(len(cleared_tweets)))

    with open('{}_cleared.json'.format(file_name), 'w', encoding='utf-8') as w:
        json.dump(cleared_tweets, w, ensure_ascii=False, indent=2)


def main():
    clear('уметь_в')


if __name__ == '__main__':
    main()
