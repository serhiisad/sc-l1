"""lab1 req module"""

import requests
URL = "http://api.tvmaze.com/schedule"


class Request:
    """class for request obj"""

    def __init__(self, region=None, date=None, start_time=None, end_time=None):
        self.__region = region;
        self.__date = date;
        self.__start_time = start_time;
        self.__end_time = end_time;

    def set_region(self, region):
        self.__region = region

    def set_date(self, date):
        self.__date = date

    def set_time(self, start_time, end_time):
        if end_time < start_time:
            raise Exception("wrong time")
        else:
            self.__start_time = start_time
            self.__end_time = end_time

    def clear_fields(self):
        self.__region = ""
        self.__date = ""
        self.__start_time = ""
        self.__end_time = ""
        print("fields are empty now")
    
    def get_region(self):
        return self.__region;

    def get_date(self):
        return self.__date;

    def get_start_time(self):
        return self.__start_time;

    def get_end_time(self):
        return self.__end_time;

    def get_infos(self, channel):
        if self.__region == "":
            return print("no region set")
        if self.__date == "":
            return print("no data set")
        if self.__start_time == "":
            return print('no time set')
        req_url = URL + '?country=' + self.__region + '&date=' + self.__date
        res = requests.get(req_url).json()
        for obj in res:
            if (obj['show']['network']['name']) == channel:
                if (obj['show']['schedule']['time'] > self.__start_time) and (obj['show']['schedule']['time'] < self.__end_time): 
                    print(obj['show']['name'])