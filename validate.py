import feedparser

def validate_feed(feed_url):
    """
    Validates whether a given RSS or Atom feed URL is valid and contains at least one entry.
    Returns True if the feed is valid, False otherwise.
    """
    try:
        feed = feedparser.parse(feed_url)
        if feed.entries:
            return True
        else:
            print(f"No entries found in {feed_url}")
            return False
    except Exception as e:
        print(f"Error validating {feed_url}: {e}")
        return False
