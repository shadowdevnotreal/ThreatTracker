from security_news import fetch_news, fetch_feeds, print_news, add_feed, remove_feed
import sys

def fetch_single_feed():
    feed_list = sn.get_feed_list()
    print("Available feeds:")
    for feed in feed_list:
        print(feed)
    feed_number = input("Enter feed number: ")
    ...

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
    main()
