import feedparser
from profoundprogrammerfeed import Profoundprogrammer

profoundprog_url = "http://theprofoundprogrammer.com/rss"
feed = feedparser.parse(profoundprog_url)


for item in feed['items']:
    print item['title']
    if '[text:' in item['title']:
        #print item
        item_parser = Profoundprogrammer()
        test = item_parser.feed(item['summary'])
        print test
        quit()
        print 'this item has an image'
