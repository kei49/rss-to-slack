
# [Entry(id='https://news.yahoo.co.jp/articles/b6d1607efef89886074a003d8e1aa496f233542a?source=rss', updated=None, title='マンション駐車場で乗用車6台が燃える火事 けが人はなし さいたま市(ABEMA TIMES)', link='https://news.yahoo.co.jp/articles/b6d1607efef89886074a003d8e1aa496f233542a?source=rss', author=None, published=datetime.datetime(2022, 10, 29, 6, 6, 6, tzinfo=datetime.timezone.utc), summary='さいたま市中央区のマンション駐車場で、乗用車6台が燃える火事があった。警察や消防が出火原因を調べている。\n\n\u3000午前9時半ごろ、さいたま市中央区・鈴谷で「駐車場内で白煙が上がっている」と通行人の男性か', content=(), enclosures=(), read=False, read_modified=None, important=False, important_modified=None, added=datetime.datetime(2022, 10, 29, 6, 17, 41, 408893, tzinfo=datetime.timezone.utc), added_by='feed', last_updated=datetime.datetime(2022, 10, 29, 6, 17, 41, 408893, tzinfo=datetime.timezone.utc), original_feed_url='https://news.yahoo.co.jp/rss/categories/domestic.xml', feed=Feed(url='https://news.yahoo.co.jp/rss/categories/domestic.xml', updated=None, title='国内 - Yahoo!ニュース', link='https://news.yahoo.co.jp/categories/domestic?source=rss', author=None, subtitle='Yahoo! JAPANのニュースに掲載されている記事の最新の見出しを提供しています。', version='rss20', user_title=None, added=datetime.datetime(2022, 10, 29, 6, 17, 41, 111432, tzinfo=datetime.timezone.utc), last_updated=datetime.datetime(2022, 10, 29, 6, 17, 41, 408893, tzinfo=datetime.timezone.utc), last_exception=None, updates_enabled=True)), Entry(id='https://news.yahoo.co.jp/articles/2826f3059ea2b27eeaa787dd52361faa0faef3c9?source=rss', updated=None, title='父の介護の傍ら独学で…土木作業員が司法試験に合格！驚異の勉強法(FRIDAY)', link='https://news.yahoo.co.jp/articles/2826f3059ea2b27eeaa787dd52361faa0faef3c9?source=rss', author=None, published=datetime.datetime(2022, 10, 29, 6, 0, 5, tzinfo=datetime.timezone.utc), summary='小室圭さんがニューヨーク州の司法試験に3度目の挑戦で合格したことが報じられ、話題になった。\n\nアメリカと日本とでは異なる部分もあるとはいえ、いずれも非常に“狭き門”である司法試験。日本では今年9月5日', content=(), enclosures=(), read=False, read_modified=None, important=False, important_modified=None, added=datetime.datetime(2022, 10, 29, 6, 17, 41, 408893, tzinfo=datetime.timezone.utc), added_by='feed', last_updated=datetime.datetime(2022, 10, 29, 6, 17, 41, 408893, tzinfo=datetime.timezone.utc), original_feed_url='https://news.yahoo.co.jp/rss/categories/domestic.xml', feed=Feed(url='https://news.yahoo.co.jp/rss/categories/domestic.xml', updated=None, title='国内 - Yahoo!ニュース', link='https://news.yahoo.co.jp/categories/domestic?source=rss', author=None, subtitle='Yahoo! JAPANのニュースに掲載されている記事の最新の見出しを提供しています。', version='rss20', user_title=None, added=datetime.datetime(2022, 10, 29, 6, 17, 41, 111432, tzinfo=datetime.timezone.utc), last_updated=datetime.datetime(2022, 10, 29, 6, 17, 41, 408893, tzinfo=datetime.timezone.utc), last_exception=None, updates_enabled=True))
def parse_entry(entry):
    id = entry.id
    updated = entry.updated
    title = entry.title
    link = entry.link
    author = entry.author
    published = entry.published
    summary = entry.summary
    content = entry.content
    read = entry.read
    
    return id, updated, title, link, author, published, summary, content, read
    print(id, updated, title, link, author, published, summary, content, read)
    
  
# EntrySearchResult(feed_url='https://news.yahoo.co.jp/rss/categories/domestic.xml', id='https://news.yahoo.co.jp/articles/e15dbc32c26b96a21c75363d079ec61a3e4681a5?source=rss', metadata=mappingproxy({'.title': HighlightedString(value='大阪・2代目「通天閣」\u3000再建66周年は足場に覆われる形で(Yahoo!ニュース オリジナル THE PAGE)', highlights=(slice(35, 39, None),)), '.feed.title': HighlightedString(value='国内 - Yahoo!ニュース', highlights=(slice(11, 15, None),))}), content=mappingproxy(OrderedDict([('.summary', HighlightedString(value='29日の近畿地方は朝から高気圧に覆われ晴れ間が広がった。気象庁によると、大阪市内では同日朝の最低気温は13.3度だったが、同日午前11時までには19.5度となった。そんなさわやかな秋空のもと、国の登', highlights=()))])))
  
def parse_entry_search_result(entry):
    feed_url = entry.feed_url
    id = entry.id
    title = entry.metadata.get('.title')
    feed_title = entry.metadata.get('.feed.title')
    summary = entry.content.get('summary')
    
    print(feed_url, id, title, feed_title, summary)