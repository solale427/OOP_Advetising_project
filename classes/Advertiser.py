import functools
from classes.BaseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):

    advertisers = []

    def __init__(self, _id, name):
        super(Advertiser, self).__init__()
        self.__id = _id
        self.__name = name
        Advertiser.advertisers.append(self)

    @staticmethod
    def get_total_clicks():
        return functools.reduce(lambda clicks1, clicks2: clicks1 + clicks2,
                                map(lambda advertiser: advertiser.get_clicks(), Advertiser.advertisers))

    @staticmethod
    def _help():
        print(
            'id: The id of this Advertiser which is unique\n'
            'name: The name of the Advertiser\n'
            'clicks: The number of clicks on this Advertiser\n'
            'views: The number of this Advertiser views\n'
        )

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def describe_me(self):
        print(
            'Advertiser: This class represents a blueprint of an advertiser which has certain methods to access each '
            'field and change it.\n'
        )








