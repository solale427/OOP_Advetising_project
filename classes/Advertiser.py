from classes.BaseAdvertising import BaseAdvertising


def _help():
    print(
        'id: The id of this Advertiser which is unique\n'
        'name: The name of the Advertiser'
        'clicks: The number of clicks on this Advertiser\n'
        'views: The number of this Advertiser views\n'
    )


def describe_me():
    print(
        'This class represents a blueprint of an advertiser which has certain methods to access each field and change '
        'it. '
    )


class Advertiser(BaseAdvertising):
    __name: str

    def __init__(self, _id, name):
        super.__init__(_id)
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
