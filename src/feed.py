import os
from reader import make_reader

def setup_feed(db, url):
    setup_dir_for_file_path(db)
    
    try:
      reader = make_reader(db)
      reader.add_feed(url)
    except Exception as e:
      print(e)
    finally:
      return reader
    

def setup_dir_for_file_path(file_path: str):
    create_dir_if_not_exists('/'.join(file_path.split('/')[:-1]))


def create_dir_if_not_exists(path):
    os.makedirs(path, exist_ok=True)