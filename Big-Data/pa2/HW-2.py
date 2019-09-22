
# coding: utf-8

# # Homework 2
# 
# In this homework, we are going to play with Twitter data.
# 
# The data is represented as rows of of [JSON](https://en.wikipedia.org/wiki/JSON#Example) strings.
# It consists of [tweets](https://dev.twitter.com/overview/api/tweets), [messages](https://dev.twitter.com/streaming/overview/messages-types), and a small amount of broken data (cannot be parsed as JSON).
# 
# For this homework, we will only focus on tweets and ignore all other messages.
# 
# 
# ## Tweets
# 
# A tweet consists of many data fields. [Here is an example](https://gist.github.com/arapat/03d02c9b327e6ff3f6c3c5c602eeaf8b). You can learn all about them in the Twitter API doc. We are going to briefly introduce only the data fields that will be used in this homework.
# 
# * `created_at`: Posted time of this tweet (time zone is included)
# * `id_str`: Tweet ID - we recommend using `id_str` over using `id` as Tweet IDs, becauase `id` is an integer and may bring some overflow problems.
# * `text`: Tweet content
# * `user`: A JSON object for information about the author of the tweet
#     * `id_str`: User ID
#     * `name`: User name (may contain spaces)
#     * `screen_name`: User screen name (no spaces)
# * `retweeted_status`: A JSON object for information about the retweeted tweet (i.e. this tweet is not original but retweeteed some other tweet)
#     * All data fields of a tweet except `retweeted_status`
# * `entities`: A JSON object for all entities in this tweet
#     * `hashtags`: An array for all the hashtags that are mentioned in this tweet
#     * `urls`: An array for all the URLs that are mentioned in this tweet
# 
# 
# ## Data source
# 
# All tweets are collected using the [Twitter Streaming API](https://dev.twitter.com/streaming/overview).
# 
# 
# ## Users partition
# 
# Besides the original tweets, we will provide you with a Pickle file, which contains a partition over 452,743 Twitter users. It contains a Python dictionary `{user_id: partition_id}`. The users are partitioned into 7 groups.

# In[1]:


import os
os.environ["PYSPARK_PYTHON"]="python3"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python3"


# In[2]:


# You can load pickle_content from a file on the local file system
# while testing on your laptop
# To test on your laptop, set `ON_EMR=False`
# To test on AWS for final submission, set `ON_EMR=True`

ON_EMR = True


# ## Grading
# 
# We ask you use the `OutputLogger` object `my_output` to store the
# results of your program.
# We have provided function calls to `my_output.append()` method for
# storing the results in all necessary places.
# Please make sure NOT to remove these lines
# 
# In the last cell of this file, we write the content of `my_output`
# to a pickle file which the grader will read in and use for grading.

# In[3]:


import os
import pickle


class OutputLogger:
    def __init__(self):
        self.ans = {}

    def append(self, key, value):
        self.ans[key] = value

    def write_to_disk(self):
        if ON_EMR:
            filepath = os.path.expanduser("answer.pickle")
            print("FilePath = {}".format(filepath))
            with open(filepath, 'wb') as f:
                pickle.dump(self.ans, f)
            proc = subprocess.Popen(["/usr/local/hadoop/hadoop-2.7.4/bin/hadoop", "fs", "-copyFromLocal", filepath, "/user/spark/answer.pickle"])
            proc.wait()
            os.remove(filepath)
        else:
            filepath = os.path.expanduser("~/answer.pickle")
            with open(filepath, 'wb') as f:
                pickle.dump(self.ans, f)


my_output = OutputLogger()


# # Part 0: Load data to a RDD

# The tweets data is stored on AWS S3. We have in total a little over 1 TB of tweets. We provide 10 MB of tweets for your local development. For the testing and grading on the homework server, we will use different data.
# 
# ## Testing on the homework server
# On EdX, we provide three different input sizes to test your program: 10 MB, 1 GB, and 10 GB. For any run, we will only be using one of these four datasets.
# 
# For submission and for local testing, make sure to read the path of the file you want to operate with from `./hw2-files.txt`. Otherwise your program will receive no points.
# 
# ## Local test
# 
# For local testing, please create your own `hw2-files.txt` file, which contains a single file path on the local disk, e.g.
# `file://<absolute_path_to_current_directory>/hw2-files-10mb.txt`. For final submission, we will create this file on our server for testing with the appropriate file path. If your implementation is correct, you should not worry about which file system (i.e. local file system or HDFS) Spark will read data from.
# 
# Now let's see how many lines there are in the input files.
# 
# 1. Make RDD from the data in the file given by the file path present in `hw2-files.txt`.
# 2. Mark the RDD to be cached (so in next operation data will be loaded in memory) 
# 3. call the `count` method to print number of lines in all these files
# 
# <b>It should print<b>
# ```
# Number of elements: 2150
# ```

# In[4]:


"""
This is a useful cell for debugging.
Use timer_start() and timer_stop() at different parts of your code
for checking the amount of time a segment takes.
"""
from time import time


timer = []
prev_ts = None


def timer_start():
    global prev_ts
    prev_ts = time()


def timer_stop(title):
    timer.append((title, time() - prev_ts))


# In[5]:


timer_start()

from pyspark import SparkContext

sc = SparkContext()

timer_stop("set up sc")


# In[6]:


timer_start()


with open('./hw2-files.txt') as f:
    file_path = [w.strip() for w in f.readlines() if w.strip()]

# Your code here
data_rdd = sc.textFile(file_path[0]).cache()
count = data_rdd.count()


my_output.append("num-tweets", count)
print('Number of elements:', count)
timer_stop("read data")


# # Part 1: Parse JSON strings to JSON objects

# Python has built-in support for JSON.

# In[7]:


import json

json_example = '''
{
    "id": 1,
    "name": "A green door",
    "price": 12.50,
    "tags": ["home", "green"]
}
'''

json_obj = json.loads(json_example)
json_obj


# ## Broken tweets and irrelevant messages
# 
# The data of this assignment may contain broken tweets (invalid JSON strings). So make sure that your code is robust for such cases.
# 
# You can filter out such broken tweet by checking if:
# * the line is not in json format
# 
# In addition, some lines in the input file might not be tweets, but messages that the Twitter server sent to the developer (such as [limit notices](https://dev.twitter.com/streaming/overview/messages-types#limit_notices)). Your program should also ignore these messages.
# 
# These messages would not contain the `created_at` field and can be filtered out accordingly.
# * Check if json object of the broken tweet has a `created_at` field
# 
# *Hint:* [Catch the ValueError](http://stackoverflow.com/questions/11294535/verify-if-a-string-is-json-in-python)
# 
# **********************************************************************************
# 
# **Tasks**
# 
# (1) Parse raw JSON tweets to obtain valid JSON objects. 
# 
# (2) From all valid tweets, construct a pair RDD of `(user_id, text)`, where `user_id` is the `id_str` data field of the `user` dictionary (read [Tweets](#Tweets) section above), `text` is the `text` data field.

# In[8]:


import json

def safe_parse(raw_json):
    """
    Input is a String
    Output is a JSON object if the tweet is valid and None if not valid
    """
    # YOUR CODE HERE
    try:
        json_obj = json.loads(raw_json) # Not broken
        json_obj["created_at"] # Not a message
        return json_obj
    except:
        return None


# In[9]:


"""
# Remember to construct an RDD of (user_id, text) here.
"""

# YOUR CODE HERE
tweet_rdd = data_rdd.map(safe_parse)                    .filter(lambda json_obj: json_obj)                    .map(lambda json_obj: (json_obj['user']['id_str'],json_obj['text'])).cache()



# ## Number of unique users
# 
# Count the number of different users in all valid tweets
# 
# (hint: [the `distinct()` method](https://spark.apache.org/docs/latest/programming-guide.html#transformations) is an easy way to do this, but try to see if there is a faster way to do this).
# 
# *******************************************************************************
# 
# **It should print**
# ```
# The number of unique users is: 1748
# ```

# In[10]:


timer_start()

# YOUR CODE HERE
users_count = len(tweet_rdd.countByKey())

my_output.append("num-unique-users", users_count)
print('The number of unique users is:', users_count)
timer_stop("Count unique users")


# # Part 2: Number of posts from each user partition

# Load the Pickle file `/twitter/users-partition.pickle`, you will get a dictionary which represents a partition over 452,743 Twitter users, `{user_id: partition_id}`. The users are partitioned into 7 groups. For example, if the dictionary is loaded into a variable named `partition`, the partition ID of the user `59458445` is `partition["59458445"]`. These users are partitioned into 7 groups. The partition ID is an integer between 0-6.
# 
# Note that the user partition we provide doesn't cover all users appear in the input data.

# ## Load the pickle file
# 
# For local testing, you can load the pickle file from the local file system, namely
# 
# ```
# proc = subprocess.Popen(["cat", "./users-partition.pickle"],
#                         stdout=subprocess.PIPE)
# pickle_content = proc.communicate()[0]
# ```
# However, for submission, please keep following code block unchanged, since on the server the pickle file is located on the HDFS.

# In[11]:


import subprocess
import pickle

if ON_EMR:
    proc = subprocess.Popen(["/usr/local/hadoop/hadoop-2.7.4/bin/hadoop", "fs", "-cat", "/user/spark/twitter/users-partition.pickle"],
                            stdout=subprocess.PIPE)
    pickle_content = proc.communicate()[0]
    
else:
    #!wget 'http://mas-dse-open.s3.amazonaws.com/Twitter/users-partition.pickle' -O './users-partition.pickle'
    proc = subprocess.Popen(["cat", "./users-partition.pickle"],
                        stdout=subprocess.PIPE)
    pickle_content = proc.communicate()[0]

partition = pickle.loads(pickle_content)
len(partition)


# ## Tweets per user partition
# 
# 1. Count the number of posts from each user partition
# 
# 2. Count the number of posts from group 0, 1, ..., 6, plus the number of posts from users who are not in any partition. Assign users who are not in any partition to the group 7.
# 
# 3. Put the results of this step into a pair RDD `(group_id, count)` that is sorted by key.
# 
# 
# 
# Print the post count using the `print_post_count` function we provided.
# 
# **It should print**
# 
# ```
# Group 0 posted 87 tweets
# Group 1 posted 242 tweets
# Group 2 posted 41 tweets
# Group 3 posted 349 tweets
# Group 4 posted 101 tweets
# Group 5 posted 358 tweets
# Group 6 posted 434 tweets
# Group 7 posted 521 tweets
# ```

# In[13]:


def print_post_count(counts):
    for group_id, count in counts:
        print('Group %d posted %d tweets' % (group_id, count))


# In[15]:


timer_start()

# YOUR CODE HERE
from operator import add


counts_per_partition = sorted(tweet_rdd.map(lambda x: (partition.get(x[0], 7), 1))               .reduceByKey(add)                 .collect())

# Following code adds your solution to `my_output`
assert(type(counts_per_partition) is list and
       len(counts_per_partition) == 8 and
       len(counts_per_partition[0]) == 2)
my_output.append("counts_per_part", counts_per_partition)
print_post_count(counts_per_partition)
timer_stop("Count tweets per user partition")


# # Part 3:  Tokens that are relatively popular in each user partition

# In this step, we are going to find tokens that are relatively popular in each user partition.
# 
# We define the number of mentions of a token $t$ in a specific user partition $k$ as the number of users from the user partition $k$ that ever mentioned the token $t$ in their tweets. Note that even if some users might mention a token $t$ multiple times or in multiple tweets, a user will contribute at most 1 to the counter of the token $t$.
# 
# Please make sure that the number of mentions of a token is equal to the number of users who mentioned this token but NOT the number of tweets that mentioned this token.
# 
# Let $N_t^k$ be the number of mentions of the token $t$ in the user partition $k$. Let $N_t^{all} = \sum_{i=0}^7 N_t^{i}$ be the number of total mentions of the token $t$.
# 
# We define the relative popularity of a token $t$ in a user partition $k$ as the log ratio between $N_t^k$ and $N_t^{all}$, i.e. 
# 
# \begin{equation}
# p_t^k = \log \frac{N_t^k}{N_t^{all}}.
# \end{equation}
# 
# 
# You can compute the relative popularity by calling the function `get_rel_popularity`.

# We load a tweet tokenizer for you in the following cells. This Tokenizer object is called `tok`. Don't forget to execute the two cells below.
# 
# You can expand the following cell if needed to see the minutae of the Tokenizer.

# In[16]:


#!/usr/bin/env python

"""
This code implements a basic, Twitter-aware tokenizer.

A tokenizer is a function that splits a string of text into words. In
Python terms, we map string and unicode objects into lists of unicode
objects.

There is not a single right way to do tokenizing. The best method
depends on the application.  This tokenizer is designed to be flexible
and this easy to adapt to new domains and tasks.  The basic logic is
this:

1. The tuple regex_strings defines a list of regular expression
   strings.

2. The regex_strings strings are put, in order, into a compiled
   regular expression object called word_re.

3. The tokenization is done by word_re.findall(s), where s is the
   user-supplied string, inside the tokenize() method of the class
   Tokenizer.

4. When instantiating Tokenizer objects, there is a single option:
   preserve_case.  By default, it is set to True. If it is set to
   False, then the tokenizer will downcase everything except for
   emoticons.

The __main__ method illustrates by tokenizing a few examples.

I've also included a Tokenizer method tokenize_random_tweet(). If the
twitter library is installed (http://code.google.com/p/python-twitter/)
and Twitter is cooperating, then it should tokenize a random
English-language tweet.


Julaiti Alafate:
  I modified the regex strings to extract URLs in tweets.
"""

__author__ = "Christopher Potts"
__copyright__ = "Copyright 2011, Christopher Potts"
__credits__ = []
__license__ = "Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License: http://creativecommons.org/licenses/by-nc-sa/3.0/"
__version__ = "1.0"
__maintainer__ = "Christopher Potts"
__email__ = "See the author's website"

######################################################################

import re
from html import entities 

######################################################################
# The following strings are components in the regular expression
# that is used for tokenizing. It's important that phone_number
# appears first in the final regex (since it can contain whitespace).
# It also could matter that tags comes after emoticons, due to the
# possibility of having text like
#
#     <:| and some text >:)
#
# Most imporatantly, the final element should always be last, since it
# does a last ditch whitespace-based tokenization of whatever is left.

# This particular element is used in a couple ways, so we define it
# with a name:
emoticon_string = r"""
    (?:
      [<>]?
      [:;=8]                     # eyes
      [\-o\*\']?                 # optional nose
      [\)\]\(\[dDpP/\:\}\{@\|\\] # mouth      
      |
      [\)\]\(\[dDpP/\:\}\{@\|\\] # mouth
      [\-o\*\']?                 # optional nose
      [:;=8]                     # eyes
      [<>]?
    )"""

# The components of the tokenizer:
regex_strings = (
    # Phone numbers:
    r"""
    (?:
      (?:            # (international)
        \+?[01]
        [\-\s.]*
      )?            
      (?:            # (area code)
        [\(]?
        \d{3}
        [\-\s.\)]*
      )?    
      \d{3}          # exchange
      [\-\s.]*   
      \d{4}          # base
    )"""
    ,
    # URLs:
    r"""http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"""
    ,
    # Emoticons:
    emoticon_string
    ,    
    # HTML tags:
     r"""<[^>]+>"""
    ,
    # Twitter username:
    r"""(?:@[\w_]+)"""
    ,
    # Twitter hashtags:
    r"""(?:\#+[\w_]+[\w\'_\-]*[\w_]+)"""
    ,
    # Remaining word types:
    r"""
    (?:[a-z][a-z'\-_]+[a-z])       # Words with apostrophes or dashes.
    |
    (?:[+\-]?\d+[,/.:-]\d+[+\-]?)  # Numbers, including fractions, decimals.
    |
    (?:[\w_]+)                     # Words without apostrophes or dashes.
    |
    (?:\.(?:\s*\.){1,})            # Ellipsis dots. 
    |
    (?:\S)                         # Everything else that isn't whitespace.
    """
    )

######################################################################
# This is the core tokenizing regex:
    
word_re = re.compile(r"""(%s)""" % "|".join(regex_strings), re.VERBOSE | re.I | re.UNICODE)

# The emoticon string gets its own regex so that we can preserve case for them as needed:
emoticon_re = re.compile(regex_strings[1], re.VERBOSE | re.I | re.UNICODE)

# These are for regularizing HTML entities to Unicode:
html_entity_digit_re = re.compile(r"&#\d+;")
html_entity_alpha_re = re.compile(r"&\w+;")
amp = "&amp;"

######################################################################

class Tokenizer:
    def __init__(self, preserve_case=False):
        self.preserve_case = preserve_case

    def tokenize(self, s):
        """
        Argument: s -- any string or unicode object
        Value: a tokenize list of strings; conatenating this list returns the original string if preserve_case=False
        """        
        # Try to ensure unicode:
        try:
            s = str(s)
        except UnicodeDecodeError:
            s = s.encode('string_escape')
            s = str(s)
        # Fix HTML character entitites:
        s = self.__html2unicode(s)
        # Tokenize:
        words = word_re.findall(s)
        # Possible alter the case, but avoid changing emoticons like :D into :d:
        if not self.preserve_case:            
            words = map((lambda x : x if emoticon_re.search(x) else x.lower()), words)
        return words

    def tokenize_random_tweet(self):
        """
        If the twitter library is installed and a twitter connection
        can be established, then tokenize a random tweet.
        """
        try:
            import twitter
        except ImportError:
            print("Apologies. The random tweet functionality requires the Python twitter library: http://code.google.com/p/python-twitter/")
        from random import shuffle
        api = twitter.Api()
        tweets = api.GetPublicTimeline()
        if tweets:
            for tweet in tweets:
                if tweet.user.lang == 'en':            
                    return self.tokenize(tweet.text)
        else:
            raise Exception("Apologies. I couldn't get Twitter to give me a public English-language tweet. Perhaps try again")

    def __html2unicode(self, s):
        """
        Internal metod that seeks to replace all the HTML entities in
        s with their corresponding unicode characters.
        """
        # First the digits:
        ents = set(html_entity_digit_re.findall(s))
        if len(ents) > 0:
            for ent in ents:
                entnum = ent[2:-1]
                try:
                    entnum = int(entnum)
                    s = s.replace(ent, unichr(entnum))	
                except:
                    pass
        # Now the alpha versions:
        ents = set(html_entity_alpha_re.findall(s))
        ents = filter((lambda x : x != amp), ents)
        for ent in ents:
            entname = ent[1:-1]
            try:            
                s = s.replace(ent, unichr(entities.name2codepoint[entname]))
            except:
                pass                    
            s = s.replace(amp, " and ")
        return s


# In[17]:


from math import log

tok = Tokenizer(preserve_case=False)

def get_rel_popularity(c_k, c_all):
    return log(1.0 * c_k / c_all) / log(2)


def print_tokens(tokens, gid = None):
    group_name = "overall"
    if gid is not None:
        group_name = "group %d" % gid
    print('=' * 5 + ' ' + group_name + ' ' + '=' * 5)
    for t, n in tokens:
        print("%s\t%.4f" % (t, n))
    print


# ## Tokenize tweets
# 
# 1. Tokenize the tweets using the `tokenize` function that is a method of the `Tokenizer` class that we have instantiated as `tok`. 
# 
# 1. Count the number of mentions for each tokens regardless of specific user group.
# 
# 1. Call `print_count` function to show how many different tokens we have.
# 
# **It should print**
# ```
# Number of tokens: 7677
# ```

# In[19]:


# YOUR CODE HERE
user_tokens = tweet_rdd.mapValues(lambda x: set(tok.tokenize(x)))                    .reduceByKey(lambda x, y: x|y)                    .flatMap(lambda x: ((x[0],y) for y in x[1])).cache()
all_tokens = user_tokens.map(lambda x: (x[1],1))                        .reduceByKey(lambda x,y: x+y).cache()
num_of_tokens = all_tokens.count()

my_output.append("num-tokens", num_of_tokens)
print("Number of tokens:", num_of_tokens)


# ## Token popularity
# 
# Tokens that are mentioned by too few users are usually not very interesting. So we want to only keep tokens that are mentioned by at least 100 users. Filter out tokens that don't meet this requirement.
# 
# Call `print_count` function to show how many different tokens we have after the filtering.
# 
# Call `print_tokens` function to show top 20 most frequent tokens.
# 
# **It should print**
# ```
# Number of tokens: 46
# ===== overall =====
# :	1046.0000
# rt	920.0000
# .	767.0000
# the	587.0000
# trump	560.0000
# …	520.0000
# to	501.0000
# ,	497.0000
# in	385.0000
# a	383.0000
# is	382.0000
# of	300.0000
# !	285.0000
# for	275.0000
# and	263.0000
# on	218.0000
# i	216.0000
# he	191.0000
# that	190.0000
# "	181.0000
# ```

# In[20]:


timer_start()

# YOUR CODE HERE
                        
freq_tokens = all_tokens.filter(lambda x: x[1] >= 100)                        .sortBy(lambda x: x[1],ascending=False).cache()
num_freq_tokens = freq_tokens.count()
top20 = freq_tokens.take(20)

my_output.append("num-freq-tokens", num_freq_tokens)
my_output.append("top-20-tokens", top20)
print("Number of tokens:", num_freq_tokens)
print_tokens(top20)
timer_stop("Count overall most popular tokens")


# ## Relative Popularity
# 
# For all tokens that are mentioned by at least 100 users, compute their relative popularity in each user group. Then print the top 10 tokens with highest relative popularity in each user group. In case two tokens have same relative popularity, break the tie by printing the alphabetically smaller one.
# 
# **Hint:** Let the relative popularity of a token $t$ be $p$. The order of the items will be satisfied by sorting them using (-p, t) as the key.
# 
# **It should print**
# ```
# ===== group 0 =====
# with	-3.6088
# cruz	-3.6554
# his	-3.6582
# amp	-3.8651
# on	-3.9608
# to	-4.0145
# &	-4.0875
# https	-4.1699
# i	-4.1699
# what	-4.1699
# ===== group 1 =====
# sanders	-2.2854
# gop	-2.4060
# hillary	-2.4330
# ’	-2.4463
# bernie	-2.4835
# "	-2.6925
# are	-2.7249
# this	-2.7633
# for	-2.8179
# about	-2.8346
# ===== group 2 =====
# with	-4.3458
# donald	-4.5146
# ...	-4.7004
# gop	-4.7279
# i	-4.9475
# on	-4.9608
# he	-4.9925
# …	-5.1155
# https	-5.1699
# what	-5.1699
# ===== group 3 =====
# bernie	-1.5945
# sanders	-1.6609
# hillary	-2.2188
# and	-2.5154
# "	-2.5930
# in	-2.6114
# will	-2.6160
# https	-2.6674
# ...	-2.7004
# you	-2.7004
# ===== group 4 =====
# what	-3.4330
# have	-3.4725
# bernie	-3.5380
# this	-3.5518
# it	-3.6881
# ?	-3.6912
# for	-3.7110
# about	-3.7415
# hillary	-3.7549
# that	-3.7625
# ===== group 5 =====
# what	-1.8007
# not	-1.8745
# https	-2.0000
# his	-2.0144
# cruz	-2.0704
# it	-2.1031
# on	-2.1243
# &	-2.1399
# amp	-2.1489
# ;	-2.1592
# ===== group 6 =====
# will	-1.3847
# have	-1.4725
# !	-1.5850
# cruz	-1.6919
# trump	-1.7199
# https	-1.7549
# -	-1.7673
# ;	-1.7807
# be	-1.7952
# amp	-1.8144
# ===== group 7 =====
# donald	-1.0740
# trump	-1.6535
# bernie	-1.7790
# sanders	-1.7829
# ’	-1.8613
# of	-1.9069
# ?	-1.9186
# with	-1.9307
# the	-1.9588
# be	-1.9758
# ```

# In[21]:


timer_start()

# YOUR CODE HERE
freq_tokens_dict = dict(freq_tokens.collect())
freq_tokens_set = set(freq_tokens_dict.keys())

popular_10_in_each_group = sorted(user_tokens.filter(lambda x: x[1] in freq_tokens_set)                                        .map(lambda x: ((partition.get(x[0], 7),x[1]),1))                                        .reduceByKey(add)                                        .map(lambda x: (x[0][0],(x[0][1],get_rel_popularity(x[1],freq_tokens_dict[x[0][1]]))))                                        .groupByKey()                                        .mapValues(lambda x: sorted(x,key=lambda x: (-x[1],x[0]))[:10]).take(10))

popular_10_in_each_group = [popular_10_in_each_group[i][1] for i in range(0,8)]

# Following code add your solution to `my_output`
my_output.append("popular_10_in_each_group", popular_10_in_each_group)
for k in range(8):
    print_tokens(popular_10_in_each_group[k], k)
timer_stop("Print popular tokens in each group")


# ## Important: Write your solutions to disk
# 
# Following cell write your solutions to disk which would be read in by the grader for grading.

# In[22]:


my_output.write_to_disk()


# ## Optional Ungraded Exercise
# The users partition is generated by a machine learning algorithm that tries to group the users by their political preferences. Three of the user groups are showing supports to Bernie Sanders, Ted Cruz, and Donald Trump. 
# 
# If your program looks okay on the local test data, you can try it on the larger input by submitting your program to the homework server. Observe the output of your program to larger input files, can you guess the partition IDs of the three groups mentioned above based on your output?

# In[ ]:


# Change the values of the following three items to your guesses
users_support = [
    (-1, "Bernie Sanders"),
    (-1, "Ted Cruz"),
    (-1, "Donald Trump")
]

for gid, candidate in users_support:
    print("Users from group %d are most likely to support %s." % (gid, candidate))


# Uncomment the lines in the cell below to print out the time taken between `time_start()` and `time_end()` at various stages of your pipeline. 

# In[23]:


total_time = 0.0
for item in timer:
    print("{}\t{}".format(item[0], item[1]))
    total_time += item[1]
print("Total time: {}".format(total_time))


# In[ ]:




