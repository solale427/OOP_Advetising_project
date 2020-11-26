from classes import BaseAdvertising
from classes import Advertiser


def describe_me():
    print(
        'id: id of this Advertisement which is unique\n'
        'advertiser: The advertiser od this Advertisement\n'
        'title: The title of the Advertisement\n'
        'imgUrl: The URL Address of image\n'
        'link: The link which directs user to advertisement\n'
        'clicks: The number of clicks on this Advertisement\n'
        'views: The number of this Advertisements views\n'
    )


class Ad(BaseAdvertising):
    __advertiser: Advertiser
    __title: str
    __imgUrl: str
    __link: str

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_imgUrl(self):
        return self.__imgUrl

    def set_imgUrl(self, imgUrl):
        self.__imgUrl = imgUrl

    def get_link(self):
        return self.__link

    def det_link(self, link):
        self.__link = link

    def set_advertiser(self, advertiser):
        self.__advertiser = advertiser

    def inc_clicks(self):
        super.inc_clicks()
        self.__advertiser.inc_clicks()

