from random import randrange
import re
import urllib
from collections import Counter
import sys
from datetime import time

def merge(d1, d2, merge_fn=lambda x,y:y):
    

    result = d1
    for k,v in d2.iteritems():
        if k in result:
            result[k] = merge_fn(result[k], v)
        else:
            result[k] = v
    return result

def scrub(comment):
    
    entity_match = re.compile(r'&#(\d+);|&(\w+);|<(.+)>|</(\w+)>')
    comment = entity_match.sub(' ', comment)
    
    return comment

def count(lst):
    countlst = []
    for string in lst:
      s = string.split()
      countlst += s
    return Counter(countlst)
    
def run():
 
    socket = urllib.urlopen("http://www.reddit.com/r/" + sys.argv[1] + "/comments/")
    subreddit = socket.geturl()
    
    htmlSource = socket.read()
    socket.close()
    
    result = re.findall('<div class="md"><p>((?:.|\\n)*?)</p>\\n</div>', htmlSource)
    lst_of_comments = []
    if len(result) >= 1: 
        for x in result:
           lst_of_comments.append(scrub(x))
    items = count(lst_of_comments)
    return reduce_dict(items)

def reduce_dict(items):
    #there has to be a smarter way to do this:
    common_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I',
                'it','for','not', 'is', 'just', 'even', 'here', 'you', 'should', 'their',
                    'only', 'when', 'after', 'then', 'than', 'those', 'there', 'has',
                    'been', 'they', 'would', 'our', 'from', 'all', 'an', 'what', 's',
                    'them', 'was', 'but', 'For', 'What', 'It']
    two_or_more = {}
    for key, value in items.iteritems():
        if value > 1:
            two_or_more[key] = value
    specific = {}
    for key, value in two_or_more.iteritems():
        if key not in common_words:
            specific[key] = value
    return specific
    
iters = 0
words_of_the_day = {}
while iters < 10:
    if words_of_the_day:
        merge(words_of_the_day, run(), lambda x,y: x+y)
    else:
        words_of_the_day = run()

    time.sleep(5)
    print words_of_the_day
    iters += 1
            



