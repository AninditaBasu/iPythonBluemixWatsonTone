import json
from twitter import TwitterStream, OAuth

#
# Authenticate yourself with Twitter
#
CONSUMER_KEY = raw_input('Enter the Twitter  consumer key: ')
CONSUMER_SECRET = raw_input('Enter the Twitter  consumer key secret: ')
ACCESS_TOKEN = raw_input('Enter the Twitter  access token: ')
ACCESS_SECRET = raw_input('Enter the Twitter  access token secret: ')
 
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

#
# Pull some tweets
#
twitter_stream = TwitterStream(auth=oauth)
iterator = twitter_stream.statuses.filter(follow="14677919")

#
# Dump the Twitter-returned data into a file for use later. Also, print the tweets to the console
#
i = 50
    #
    # the number of tweets to read
    # a small number so that the code runs faster
    #
tweets = open("./static/tweets.json", "w")
    #
    # write to the static folder so that the file persists
    #
for tweet in iterator:
    tweet_raw = json.dumps(tweet)
    print >> tweets, tweet_raw
        #
        # write the entire tweet to a file, for use later
        #
    tweet_text = json.loads(tweet_raw.strip())
    if 'text' in tweet_text:
        print tweet['text'].encode('utf-8')  
        #
        # so that only the text of the tweet
        # is displayed on the console
        # no need to see everything
        #
    i -= 1
    if i == 0:
        break
 
tweets.close()

#
# Extract the contents of the text node of tweets, clean up, and write to a file for use later
#
# clean up the tweets to remove punctuations, hashtags, and other unwanted stuff #
 
import json
 
end_strip = [".", ",", "?", "/", "!", "*", ":", ")", "'", '"']
start_strip = [":", "*", "(", "'", '"']
 
words = [] # a list to contain all the words in all the tweets
 
tweets_file = open('./static/tweets.json', 'r')
for line in tweets_file:
    tweet = json.loads(line)
    #print tweet
    if 'text' in tweet:
        tweet_text = tweet['text']
        #print tweet
        for word in tweet_text.split():
            word = word.lower()
            if word == "rt": # do not add to list if word is "rt"
                break
            for item in end_strip:
                if word.endswith(item):
                    word = word[:-1]
            for item in start_strip:
                if word.startswith(item):
                    word = word[1:]
            words.append(word)
 
tweets_file.close()
 
prefix_list = ("http", "@", "t.co", "bit.ly")
# do not reckon words that start with any of the strings in the prefix list
for word in words[:]:
    if word.startswith(prefix_list):
        words.remove(word)
 
text = ""
for word in words:
    #print word
    text = text + " " + word
#print text
text = text.encode('utf-8')
 
# write the text to a file, for later use
textfile = open("./static/tweets_text.txt", "w")
textfile.write(text)
textfile.close()
 
print "Done cleaning up tweets."

#
# Generate a word cloud image
#
%matplotlib inline # for iPython notebook use
 
f = open("./static/tweets_clean.txt", "r")
text = f.read()
 
from wordcloud import WordCloud
wordcloud = WordCloud().generate(text)
 
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
 
wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
 
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# end of watson_get_tweets.py