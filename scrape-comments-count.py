from random import randrange
import re
import urllib
from collections import Counter


def scrub(comment):
    
    entity_match = re.compile(r'&#(\d+);|&(\w+);|<(.+)>|</(\w+)>')
    comment = entity_match.sub(' ', comment)
    
    return comment

def count(lst):
    countlst = []
    for string in lst:
      s = string.split()
      countlist += s
     return Counter(countlist)

def run():
    socket = urllib.urlopen("http://www.reddit.com/r/news/comments")
    subreddit = socket.geturl()
    
    htmlSource = socket.read()
    socket.close()
    
    result = re.findall('<div class="md"><p>((?:.|\\n)*?)</p>\\n</div>', htmlSource)
    lst_of_comments = []
    if len(result) >= 1:
        
        for x in result:
            scrub(x)
            lst_of_comments.append(x)
    print count(lst_of_comments)

run()

