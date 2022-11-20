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
    Feed('tdnet', "https://webapi.yanoshin.jp/webapi/tdnet/list/recent.rss", 'data/tdnet.sqlite'),
    Feed('sg-theindependent', 'https://theindependent.sg/feed/', 'data/sg-theindependet.sqlite'),
    Feed('sg-tr-emeritus', 'https://www.tremeritus.net/feed/', 'data/sg-tr-emeritus.sqlite'),
    Feed('sg-singaporestart', 'http://feeds.singaporestar.com/rss/a677a0718b69db72', 'data/sg-singaporestart.sqlite'),
    Feed('sg-newsnet', 'http://feeds.singaporenews.net/rss/a677a0718b69db72', 'data/sg-newsnet.sqlite'),
    Feed('sg-business-review', 'https://sbr.com.sg/rss2/news', 'data/sg-business-review.sqlite'),
    Feed('sg-localnews', 'https://localnewsingapore.com/feed/', 'data/sg-localnews.sqlite'),
    Feed('sg-straitstimes-singapore', 'https://www.straitstimes.com/news/singapore/rss.xml', 'data/sg-straitstimes-singapore.sqlite'),
    Feed('sg-straitstimes-business', 'https://www.straitstimes.com/news/business/rss.xml', 'data/sg-straitstimes-business.sqlite'),
    Feed('sg-straitstimes-world', 'https://www.straitstimes.com/news/world/rss.xml', 'data/sg-straitstimes-world.sqlite'),
    Feed('sg-straitstimes-asia', 'https://www.straitstimes.com/news/asia/rss.xml', 'data/sg-straitstimes-asia.sqlite'),
    ]
  

@dataclass
class Config:
  slack_webhook_url_yahoo = os.environ['SLACK_WEBHOOK_URL_YAHOO']
  slack_webhook_url_prtimes = os.environ['SLACK_WEBHOOK_URL_PRTIMES']
  slack_webhook_url_tdnet = os.environ['SLACK_WEBHOOK_URL_TDNET']
  slack_webhook_url_singapore = os.environ['SLACK_WEBHOOK_URL_SG_NEWS']
  black_words_list = [
    'コロナ', '共同通信', '天気', 'Nosweb.jp', 'ベストカーWeb', 'Webモーターマガジン', 'くるまのニュース', '乗りものニュース', '日刊自動車新聞', 'スポーツ', 'VAGUE', 'WEB CARTOP',
    'ウェザーニュース', 'テレビ朝日系', 'Aviation Wire', 'LIMO', '(レスポンス)', 'AUTOCAR JAPAN', '(Auto Messe Web)', '(WWDJAPAN.com)', 'ねとらぼ', '(CHANTO WEB)', '(ドライバーWeb)',
    '(WATCHNAVI Salon)', '(ABEMA TIMES)', '(ダイヤモンド・オンライン)', '人身事故', '(WEBヤングマシン)', '(ITmedia ビジネスオンライン)', '(バイクのニュース)',
    '(Fav-Log by ITmedia)', '(聯合ニュース)', '(Impress Watch)', '(ITmedia Mobile)', '(ウェザーマップ)', 'tenki.jp', '(PHILE WEB)', '(BuzzFeed Japan)', '(webCG)',
    '(＆GP)', '(FRIDAY)', '(ファイナンシャルフィールド)', '梨泰院', '(鉄道コム)', '(食品産業新聞社ニュースWEB)', '(アスキー)', '(GetNavi web)', '(All About)', '(産経新聞)',
    '(週刊SPA!)', '(NEWSポストセブン)', '(アフロ)', '(ITmedia PC USER)', '(MONOist)', '(モーサイ)', '(BCN)', '(ニュースイッチ)', '(MotorFan)', '(AERA dot.)', '(Merkmal)',
    '(スポニチアネックス)', '(ニッポン放送)','(日刊産業新聞)', '［and］', '(読売テレビ)'
    ]
  white_words_list = [
    'マスク氏', '円安'
  ]