from random import randrange
import re
import urllib


def scrub(comment):
    
    entity_match = re.compile(r'&#(\d+);|&(\w+);|<(.+)>|</(\w+)>')
    comment = entity_match.sub('', comment)
    
    return comment

def run():
    socket = urllib.urlopen("http://www.reddit.com/r/random")
    subreddit = socket.geturl()
    if subreddit == "http://www.reddit.com/r/random":
        return
    #print subreddit
    socket.close()
    subreddit_comments_socket = urllib.urlopen(subreddit + "comments/")
    #print subreddit_comments_socket.geturl()
    htmlSource = subreddit_comments_socket.read()

    subreddit_comments_socket.close()

    result = re.findall('<div class="md"><p>((?:.|\\n)*?)</p>\\n</div>', htmlSource)
    if len(result) >= 1:
        comment = result[1]
        print scrub(comment)
    else:
        return
run()


