"""module"""


class Member:
    """class to save every region info"""

    def __init__(self, region=None, date=None, start_time=None, end_time=None):
        self.__region = region
        self.__date = date
        self.__start_time = start_time
        self.__end_time = end_time
        self.__channels = []

    def add_channel(self, channel):
        self.__channels.append(channel)

    def add_channels(self, channels):
        self.__channels.extend(channels)

    def set_region(self, region):
        self.__region = region

    def set_date(self, date):
        self.__date = date

    def set_time(self, startTime, endTime):
        if startTime > endTime:
            raise Exception("wrong time")
        self.__start_time = startTime
        self.__end_time = endTime

    def get_channels(self):
        return self.__channels

    def get_date(self):
        return self.__date

    def get_region(self):
        return self.__region

    def get_start_time(self):
        return self.__start_time

    def get_end_time(self):
        return self.__end_time
