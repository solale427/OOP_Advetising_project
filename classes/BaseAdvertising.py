class BaseAdvertising:
    __id: int
    __clicks: int = 0
    __views: int = 0

    def get_clicks(self) -> int:
        return self.__clicks

    def get_views(self) -> int:
        return self.__views

    def inc_clicks(self):
        self.__clicks += 1

    def inc_views(self):
        self.__views += 1

    def describe_me(self):
        print(
            'BaseAdvertising: This class is parent to Ad and Advertiser classes.\n'
        )
