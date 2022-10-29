from reader import make_reader

def setup_feed(db, url):
    try:
      reader = make_reader(db)
      reader.add_feed(url)
    except Exception as e:
      print(e)
    finally:
      return reader