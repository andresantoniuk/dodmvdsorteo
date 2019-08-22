from twython import Twython
import random

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

tweets = []
MAX_ATTEMPTS = 100
COUNT_OF_TWEETS_TO_BE_FETCHED = 99999

for i in range(0,MAX_ATTEMPTS):

    if(COUNT_OF_TWEETS_TO_BE_FETCHED < len(tweets)):
        break

    # STEP 1: Query Twitter
    if(0 == i):
        # Query twitter for data. 
        results = twitter.search(q="#DevOpsDaysMVD",since_id=1164121276329472001,count='100')
    else:
        # After the first call we should have max_id from result of previous call. Pass it in query.
        results = twitter.search(q="#DevOpsDaysMVD",include_entities='true',max_id=next_max_id)

    # STEP 2: Save the returned tweets
    for result in results['statuses']:
        tweets.append(result)


    # STEP 3: Get the next max_id
    try:
        # Parse the data returned to get max_id to be passed in consequent call.
        next_results_url_params = results['search_metadata']['next_results']
        next_max_id = next_results_url_params.split('max_id=')[1].split('&')[0]
    except:
        # No more next pages
        break

print("total de tweets con #DevOpsDaysMVD: ", len(tweets))

print('---------')

usuarios = []
for tw in tweets:
    usuarios.append(tw['user']['screen_name'])
    print(tw['user']['screen_name'])


ganador = random.randint(0,len(tweets))


print(tweets[ganador]['text'])
print('----')
print(tweets[ganador]['user']['name'])
print(tweets[ganador]['user']['screen_name'])
print("https://twitter.com/%s/status/%s" % (tweets[ganador]['user']['screen_name'],tweets[ganador]['id']))
	