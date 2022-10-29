from dataclasses import dataclass

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
  slack_webhook_url_yahoo = "https://hooks.slack.com/services/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"
  slack_webhook_url_prtimes = "https://hooks.slack.com/services/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"
  slack_webhook_url_tdnet = "https://hooks.slack.com/services/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"
  black_words_list = [
    'コロナ', '共同通信', '天気', 'Nosweb.jp', 'ベストカーWeb', 'Webモーターマガジン', 'くるまのニュース', '乗りものニュース', '日刊自動車新聞', 'スポーツ', 'VAGUE', 'WEB CARTOP',
    'ウェザーニュース', 'テレビ朝日系', 'Aviation Wire', 'LIMO', '(レスポンス)', 'AUTOCAR JAPAN', '(Auto Messe Web)', '(WWDJAPAN.com)', 'ねとらぼ', '(CHANTO WEB)', '(ドライバーWeb)',
    '(WATCHNAVI Salon)', '(ABEMA TIMES)']
  white_words_list = [
    'マスク氏', '円安'
  ]