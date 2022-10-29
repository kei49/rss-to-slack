from src.config import create_feeds
from src.feed import setup_feed

def mark_all_read():
  feeds = create_feeds()

  for feed in feeds:
      reader = setup_feed(feed.db, feed.url)
      reader.update_feeds()
      
      entries = list(reader.get_entries(read=False))
      
      print(f"marking read for {len(entries)} entries in {feed.name}")
      
      for entry in entries:
        reader.mark_entry_as_read(entry)
