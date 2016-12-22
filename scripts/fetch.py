import twitter
import json
import time

api = twitter.Api(consumer_key='biV7ndS9hJHcyXZKGGYZf6WWI',
                  consumer_secret='PbTwqsdS8t2tW8zf9EVLjYT4fwFDhxYwxlv5qfsYh8cNsts78x',
                  access_token_key='2782482091-QsmddClZz4huWWCQW5HkLBAAZykPTXtDHv23XgS',
                  access_token_secret='XUbLEUqxInIDRAIogbecMoy2n6SYS7wrPkQHa94pzY7dj')


def get_100_results_down(query, max_id):
    results = api.GetSearch(
        raw_query='q="{}"&count=100&max_id={}'.format(
            query, max_id
        )
    )

    min_id = max_id
    for result in results:
        print(result._json['created_at'])
        if result.id < min_id:
            min_id = result.id

    return len(results), min_id-1, results


def get_100_results_up(query, min_id):
    results = api.GetSearch(
        raw_query='q="{}"&count=100&since_id={}'.format(
            query, min_id
        )
    )

    max_id = min_id
    for result in results:
        print(result._json['created_at'])
        if result.id > max_id:
            max_id = result.id

    return len(results), max_id+1, results


def main():
    q = 'умею'
    # doc_id = 0
    t1 = time.time()
    start_id = 806106448010874879
    len_results = True
    i = 0
    all_docs = []

    while len_results:
        print('by now fetched: {}'.format(i))
        # print(start_id)
        len_results, start_id, results = get_100_results_down(q, start_id)
        i += len_results
        # print(start_id)

        for result in results:
            # i.append(result.id)
            one_doc = result._json
            all_docs.append(one_doc)

    print('now up')

    start_id = 806106448010874879
    len_results = True
    while len_results:
        print('by now fetched: {}'.format(i))
        len_results, start_id, results = get_100_results_up(q, start_id)
        i += len_results

        for result in results:
            # i.append(result.id)
            one_doc = result._json
            all_docs.append(one_doc)

    with open('{}.json'.format(q.replace(' ', '_')), 'w', encoding='utf-8') as w:
        json.dump(all_docs, w, ensure_ascii=False, indent=2)

    print(i)

    t2 = time.time()

    print(t2-t1)


if __name__ == '__main__':
    main()
