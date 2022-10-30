import os
from dataclasses import dataclass

import src.init_env

@dataclass
class Feed:
  name: str
  url: str
  db: str


def create_feeds() -> list[Feed]:
  return [
    Feed('yahoo-domestic', "https://news.yahoo.co.jp/rss/categories/domestic.xml", 'data/yahoo-domestic.sqlite'), 
    Feed('yahoo-world', "https://news.yahoo.co.jp/rss/categories/world.xml", 'data/yahoo-world.sqlite'),
    Feed('yahoo-business', "https://news.yahoo.co.jp/rss/categories/business.xml", 'data/yahoo-business.sqlite'),
    Feed('yahoo-it', "https://news.yahoo.co.jp/rss/categories/it.xml", 'data/yahoo-it.sqlite'),
    # Feed('prtimes', "https://prtimes.jp/index.rdf", 'data/prtimes.sqlite')
    Feed('tdnet', "https://webapi.yanoshin.jp/webapi/tdnet/list/recent.rss", 'data/tdnet.sqlite')
    ]
  

@dataclass
class Config:
  slack_webhook_url_yahoo = os.environ['SLACK_WEBHOOK_URL_YAHOO']
  slack_webhook_url_prtimes = os.environ['SLACK_WEBHOOK_URL_PRTIMES']
  slack_webhook_url_tdnet = os.environ['SLACK_WEBHOOK_URL_TDNET']
  black_words_list = [
    'コロナ', '共同通信', '天気', 'Nosweb.jp', 'ベストカーWeb', 'Webモーターマガジン', 'くるまのニュース', '乗りものニュース', '日刊自動車新聞', 'スポーツ', 'VAGUE', 'WEB CARTOP',
    'ウェザーニュース', 'テレビ朝日系', 'Aviation Wire', 'LIMO', '(レスポンス)', 'AUTOCAR JAPAN', '(Auto Messe Web)', '(WWDJAPAN.com)', 'ねとらぼ', '(CHANTO WEB)', '(ドライバーWeb)',
    '(WATCHNAVI Salon)', '(ABEMA TIMES)', '(ダイヤモンド・オンライン)', '人身事故', '(WEBヤングマシン)', '(ITmedia ビジネスオンライン)', '(バイクのニュース)']
  white_words_list = [
    'マスク氏', '円安'
  ]