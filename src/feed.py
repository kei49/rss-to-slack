from datetime import datetime, timedelta, timezone
import pytz

tokyo_tz = pytz.timezone('Asia/Tokyo')
    
# def delete_feed_with_too_many_entries(reader, db, url):
#     entries = list(reader.get_entries())
    
#     if len(entries) > 300:
#       print("deleting feeds: ", url)
#       reader.delete_feed(url)
#       return setup_feed(db, url)
    
#     return reader
    
    
def delete_old_entries(reader):
    entries = list(reader.get_entries())
    for entry in entries:
        if entry.published.replace(tzinfo=None) < datetime.now() - timedelta(days=1):
            print(entry)
            reader.delete_entry(entry)
    