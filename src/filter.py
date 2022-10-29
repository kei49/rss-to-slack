from src.config import Config

def filter_out_black_words(title: str):
  config = Config()
  
  do_remove = False
  for word in config.black_words_list:
    if word in title:
      do_remove = True
      break
    
  return do_remove