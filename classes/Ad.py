from classes.BaseAdvertising import BaseAdvertising
from classes.Advertiser import Advertiser


class Ad(BaseAdvertising):
    __advertiser: Advertiser
    __title: str
    __imgUrl: str
    __link: str

    def __init__(self, _id: int, title: str, imgUrl: str, link: str, advertiser: Advertiser):
        super(Ad, self).__init__()
        self.__id = _id
        self.__link = link
        self.__advertiser = advertiser
        self.__title = title
        self.__imgUrl = imgUrl

    def get_title(self)-> str:
        return self.__title

    def set_title(self, title: str):
        self.__title = title

    def get_imgUrl(self) -> str:
        return self.__imgUrl

    def set_imgUrl(self, imgUrl: str):
        self.__imgUrl = imgUrl

    def get_link(self) -> str:
        return self.__link

    def det_link(self, link: str):
        self.__link = link

    def set_advertiser(self, advertiser: Advertiser):
        self.__advertiser = advertiser

    def inc_clicks(self):
        super(Ad, self).inc_clicks()
        self.__advertiser.inc_clicks()

    def inc_views(self):
        super(Ad, self).inc_views()
        self.__advertiser.inc_views()

    @staticmethod
    def _help():
        print(
            'id: id of this Advertisement which is unique\n'
            'advertiser: The advertiser od this Advertisement\n'
            'title: The title of the Advertisement\n'
            'imgUrl: The URL Address of image\n'
            'link: The link which directs user to advertisement\n'
            'clicks: The number of clicks on this Advertisement\n'
            'views: The number of this Advertisements views\n'
        )

    @staticmethod
    def describe_me():
        print(
            'Ad: This class represents a blueprint of an advertisement which has certain methods to access each field '
            'and change it.\n'
        )
