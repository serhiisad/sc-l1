"""module"""


class Memeber:
    """class to save every region info"""

    def __init__(self, region, date, start_time, end_time):
        self.__region = region
        self.__date = date
        self.__start_time = start_time
        self.__end_time = end_time
        self.__channels = []

    def add_channel(self, channel):
        self.__channels.append(channel)

    def add_channels(self, channels):
        self.__channels.extend(channels)
    
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