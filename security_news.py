import feedparser
import json


def fetch_feeds():
    with open('feeds.json') as f:
        feeds = json.load(f)['feeds']
    return [{'name': name, 'url': url} for name, url in feeds.items()]

def fetch_news(feeds):
    news = []
    for feed in feeds:
        try:
            if not feed.get('url'):
                raise ValueError(f"Invalid feed: {feed}")
            fp = feedparser.parse(feed['url'])
            for entry in fp.entries[:5]:  # limit to 5 articles per feed
                news.append({
                    'title': entry.title,
                    'description': entry.description,
                    'link': entry.link,
                    'published': entry.published,
                    'feed': feed['name']
                })
            print(f"Fetched {len(news)} news for {feed['name']}")
        except Exception as e:
            print(f"Error fetching feed {feed['name']}: {str(e)}")
    return news

def get_feed_list():
    """
    Returns a list of strings that includes the index number and name of each feed.
    """
    feed_list = read_feed_list()
    feed_strings = [f"{i+1}. {feed['name']}" for i, feed in enumerate(feed_list)]
    return feed_strings


def print_news(news):
    for n in news:
        print(f"{n['feed']} - <a href='{n['link']}' target='_blank'>{n['title']}</a>")
        print(n['description'])
        print(n['published'])
        print()



def add_feed():
    feeds = fetch_feeds()
    name = input("Enter feed name: ")
    url = input("Enter feed url: ")
    feeds.append({'name': name, 'url': url})
    with open('feeds.json', 'w') as f:
        json.dump({'feeds': {feed['name']: feed['url'] for feed in feeds}}, f)
    print("Feed added successfully!")


def remove_feed():
    feeds = fetch_feeds()
    print("Available feeds:")
    for i, feed in enumerate(feeds, start=1):
        print(f"{i}. {feed['name']}")
    feed_choice = input("Enter feed number to remove: ")
    try:
        feed_choice = int(feed_choice)
        feed = feeds[feed_choice - 1]
        feeds.remove(feed)
        with open('feeds.json', 'w') as f:
            json.dump({'feeds': {feed['name']: feed['url'] for feed in feeds}}, f)
        print(f"Feed {feed['name']} removed successfully!")
    except (ValueError, IndexError):
        print("Invalid feed choice!")


def main():
    while True:
        print("What do you want to do?")
        print("1. Fetch news for all feeds")
        print("2. Fetch news for a single feed")
        print("3. Add a new feed")
        print("4. Remove a feed")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Fetching news for all feeds...")
            news = fetch_news(fetch_feeds())
            print_news(news)
        elif choice == "2":
            feeds = fetch_feeds()
            print("Available feeds:")
            for i, feed in enumerate(feeds, start=1):
                print(f"{i}. {feed['name']}")
            feed_choice = input("Enter feed number: ")
            try:
                feed_choice = int(feed_choice)
                feed = feeds[feed_choice - 1]
                print(f"Fetching news for {feed['name']}...")
                news = fetch_news([feed])
                print_news(news)
            except (ValueError, IndexError):
                print("Invalid feed choice!")
        elif choice == "3":
            add_feed()
        elif choice == "4":
            remove_feed()
        elif choice == "5":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main
