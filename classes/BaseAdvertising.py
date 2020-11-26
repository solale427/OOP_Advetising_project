def describe_me():
    print(
        'This class is parent to Ad and Advertiser classes.'
    )

class BaseAdvertising:
    __id: int
    __clicks: int = 0
    __views: int = 0

    def __init__(self, _id):
        self.__id = _id

    def get_clicks(self):
        return self.__clicks

    def get_views(self):
        return self.__views

    def inc_clicks(self):
        self.__clicks += 1

    def inc_views(self):
        self.__views += 1

