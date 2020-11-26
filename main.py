from classes.Ad import Ad
from classes.Advertiser import Advertiser, get_total_clicks, _help
from classes.BaseAdvertising import BaseAdvertising

baseAdvertising = BaseAdvertising()
advertiser1 = Advertiser(_id=1, name='name1')
advertiser2 = Advertiser(_id=2, name='name2')
ad1 = Ad(1, 'title1', 'img-url1', 'link1', advertiser1)
ad2 = Ad(2, 'title2', 'img-url2', 'link2', advertiser2)

baseAdvertising.describe_me()
ad2.describe_me()
advertiser1.describe_me()

ad1.inc_views()
ad1.inc_views()
ad1.inc_views()
ad1.inc_views()
ad2.inc_views()
ad1.inc_clicks()
ad1.inc_clicks()
ad2.inc_clicks()


print(advertiser2.get_name(), '\n')
advertiser2.set_name('new name')
print(advertiser2.get_name(), '\n')
print(ad1.get_clicks(), '\n')
print(advertiser2.get_clicks(), '\n')
print(get_total_clicks(), '\n')
_help()