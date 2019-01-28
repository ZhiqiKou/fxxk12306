# @Time    : 19-1-28
# @Author  : Zhiqi Kou
# @Email   : zhiqi1028@gmail.com

import requests
import pymysql


class Station(object):

    def __init__(self):
        self.url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9091"

    def get_station_info(self):
        try:
            r = requests.get(self.url, timeout=30)
            r.raise_for_status()  # 如果状态不是200, 引发HTTPError异常
            r.encoding = r.apparent_encoding
        except:
            return "产生异常"

        stations_info = r.text.split("\'")[1]
        stations_list = stations_info.split("@")
        return stations_list

    def save_station(self, stations_list):
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="zhiqi",
            port=3306,
            database="fxxk12306",
        )
        cursor = conn.cursor()
        for station in stations_list:
            if station != '':
                station_info = station.split('|')
                # print(tuple(station_info))
                sql = """insert into station_info(tshorthand,name,code,pinyin,shorthand,id) values ('%s','%s','%s','%s','%s','%s');"""
                cursor.execute(sql%tuple(station_info))
                conn.commit()

        # 关闭连接
        cursor.close()
        conn.close()


station = Station()
stations_list = station.get_station_info()
station.save_station(stations_list)
