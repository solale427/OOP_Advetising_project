class BaseAdvertiser:
    __id: int
    __clicks: int
    __views: int

    def get_clicks(self):
        return self.__clicks

    def get_views(self):
        return self.__views

    def inc_clicks(self):
        self.__clicks += 1

    def inc_views(self):
        self.__views += 1
