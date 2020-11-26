import functools
from classes.BaseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    __name: str

    def __init__(self, _id, name):
        self.__id = _id
        self.__name = name
        advertisers.append(self)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def describe_me(self):
        print(
            'Advertiser: This class represents a blueprint of an advertiser which has certain methods to access each '
            'field and change it.\n'
        )


advertisers: [Advertiser] = []


def get_total_clicks():
    return functools.reduce(lambda clicks1, clicks2: clicks1 + clicks2,
                            map(lambda advertiser: advertiser.get_clicks(), advertisers))


def _help():
    print(
        'id: The id of this Advertiser which is unique\n'
        'name: The name of the Advertiser\n'
        'clicks: The number of clicks on this Advertiser\n'
        'views: The number of this Advertiser views\n'
    )