from classes.Advertiser import Advertiser
from classes.Ad import Ad
from classes.BaseAdvertising import BaseAdvertising

baseAdvertising = BaseAdvertising()
advertiser1 = Advertiser(_id=1, name='name1')
advertiser2 = Advertiser(_id=2, name='name2')
ad1 = Ad(1, 'title1', 'img-url1', 'link1', advertiser1)
ad2 = Ad(2, 'title2', 'img-url2', 'link2', advertiser2)

baseAdvertising