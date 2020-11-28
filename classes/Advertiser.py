import functools
from classes.BaseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    advertisers = []

    def __init__(self, _id: int, name: str):
        super(Advertiser, self).__init__()
        self.__id = _id
        self.__name = name
        Advertiser.advertisers.append(self)

    @staticmethod
    def get_total_clicks() -> int:
        return sum(map(lambda advertiser: advertiser.get_clicks(), Advertiser.advertisers), start=0)

    @staticmethod
    def _help():
        print(
            'id: The id of this Advertiser which is unique\n'
            'name: The name of the Advertiser\n'
            'clicks: The number of clicks on this Advertiser\n'
            'views: The number of this Advertiser views\n'
        )

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def describe_me(self):
        print(
            'Advertiser: This class represents a blueprint of an advertiser which has certain methods to access each '
            'field and change it.\n'
        )
