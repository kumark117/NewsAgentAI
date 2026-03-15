import feedparser

feeds = [
    "https://techcrunch.com/feed/",
    "https://hnrss.org/frontpage",
    "https://www.theverge.com/rss/index.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "https://feeds.arstechnica.com/arstechnica/index",
    "https://www.wired.com/feed/rss"
]

def fetch_topics():
    topics = []

    for url in feeds:
        feed = feedparser.parse(url)

        for entry in feed.entries[:20]:
            topics.append(entry.title)

    return topics