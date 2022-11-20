from time import sleep

import src.init_env
from src.filter import filter_out_black_words
from src.slack import MessageType, SlackClient
from src.parser import parse_entry, parse_entry_search_result
from src.config import create_feeds
from src.feed import setup_feed

      
def run():
  while True:
    # run_once()
    run_once_for_block()
    
    sleep(60*20)
    

def run_once_for_block():
  feeds = create_feeds()

  for feed in feeds:
      reader = setup_feed(feed.db, feed.url)

      reader.update_feeds()
      entries = list(reader.get_entries(read=False))
      
      if "yahoo" in feed.name:
        slack = SlackClient(MessageType.YAHOO)
      elif feed.name == "tdnet":
        continue
        # slack = SlackClient(MessageType.TDNET)
      elif 'sg-' in feed.name:
        slack = SlackClient(MessageType.SG_NEWS)
      else:
        continue
    
      contents = []
      
      for entry in entries:
          id, updated, title, link, author, published, summary, content, read = parse_entry(entry)
          
          do_remove = filter_out_black_words(title)
          
          if not do_remove:
            content = None
            if "yahoo" in feed.name:
              content = f"<{link}|{title}>\n{summary}"
            elif 'sg-' in feed.name:
              content = f"<{link}|{title}>"
            
            if content != None:
               contents.append(content)
            
          reader.mark_entry_as_read(entry)
          
      slack.send_rss_feeds_as_block(feed.name, contents)
      
      print(f"{feed.name} had {len(contents)} effective entries")
      
      sleep(3)
  


def run_once():
  feeds = create_feeds()

  for feed in feeds:
      reader = setup_feed(feed.db, feed.url)

      reader.update_feeds()
      entries = list(reader.get_entries(read=False))
      
      count = 0
      
      for entry in entries:
          id, updated, title, link, author, published, summary, content, read = parse_entry(entry)
          
          do_remove = filter_out_black_words(title)
          
          if not do_remove:
            
            if "yahoo" in feed.name:
              slack = SlackClient(MessageType.YAHOO)
              slack.send_rss_feed(feed.name, link, title, summary)
            elif feed.name == "tdnet":
              pass
              # slack = SlackClient(MessageType.TDNET)
              # slack.send_rss_feed(feed.name, id, f"{title} ({published})")
            elif 'sg-' in feed.name:
              slack = SlackClient(MessageType.SG_NEWS)
              slack.send_rss_feed(feed.name, link, title)
            else:
              continue
            
            reader.mark_entry_as_read(entry)
            
            count += 1
          
      
      print(f"{feed.name} had {count} effective entries")


def debug():
    feeds = create_feeds()
    
    feed = feeds[0]
    reader = setup_feed(feed.db, feed.url)

    reader.update_feeds()
    entries = list(reader.get_entries(read=True, limit=5))
    
    for entry in entries:
        id, updated, title, link, author, published, summary, content, read = parse_entry(entry)
        
        print(id, title, published, summary)
        
        slack = SlackClient(MessageType.YAHOO)
        slack.send_rss_feed(feed.name, link, title, summary)
        
        
  # reader.update_search()

  # for e in reader.search_entries('バイデン', limit=3):
  #   parse_entry_search_result(e)