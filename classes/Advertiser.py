from classes import BaseAdvertising


def describe_me():
    print(
        'id: The id of this Advertiser which is unique\n'
        'name: The name of the Advertiser'
        'clicks: The number of clicks on this Advertiser\n'
        'views: The number of this Advertiser views\n'
    )


class Advertising(BaseAdvertising):
    __name: str

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
