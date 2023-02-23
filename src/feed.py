import os
from reader import make_reader
from datetime import datetime, timedelta, timezone
import pytz

tokyo_tz = pytz.timezone('Asia/Tokyo')

def setup_feed(db, url):
    setup_dir_for_file_path(db)
    reader = make_reader(db)
    
    try:
      reader.add_feed(url)
    except Exception as e:
      print(e)
    finally:
      return reader
    
def delete_feed_with_too_many_entries(reader, db, url):
    entries = list(reader.get_entries())
    
    if len(entries) > 300:
      print("deleting feeds: ", url)
      reader.delete_feed(url)
      return setup_feed(db, url)
    
    return reader
    
    
def delete_old_entries(reader):
    entries = list(reader.get_entries())
    for entry in entries:
        if entry.published.replace(tzinfo=None) < datetime.now() - timedelta(days=1):
            print(entry)
            reader.delete_entry(entry)
    

def setup_dir_for_file_path(file_path: str):
    create_dir_if_not_exists('/'.join(file_path.split('/')[:-1]))


def create_dir_if_not_exists(path):
    os.makedirs(path, exist_ok=True)