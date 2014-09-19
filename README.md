CommentRoulette -scraper
===============
###For getting an idea of what's going on without having to do all that pesky reading.
Requires a subreddit passed as an argument

input:

$ python scrape-comments-count.py worldnews

example output:

{'can': 2, 'one': 3, 'as': 3, 'are': 9, 'go': 2, 'yes': 2, 'still': 3, 'linked': 2, 'by': 2, 'Putin': 2, 'title': 2, 'true': 2, 'had': 2, 'same': 3, 'actually': 3, 'how': 2, 'does': 2, 'They': 2, 'power,': 2, 't': 3, 'it.': 2, 'do': 2, 'None': 2, 'his': 2, 'fire': 2, 'observers': 2, 'most': 3, 'important': 2, 'She': 2, 'report': 2, 'The': 6, 'believe': 2, 'with': 2, 'Russia': 2, 'on': 3, 'about': 4, 'made': 2, 'AFP': 2, 'like': 2, 'this': 5, 'many': 2, 'could': 2, 'no': 5, 'up': 2, 'part': 2, 'she': 4, 'were': 4, 'declare': 2, 'You': 3, 'fallacy': 2}

seems like putin and russia are causing trouble today. Filtering out the top 15 or so most common english words.

###Future

A version of this that aggregates the most common words over a period of time. Maybe once an hour it runs and keeps track of trends.
