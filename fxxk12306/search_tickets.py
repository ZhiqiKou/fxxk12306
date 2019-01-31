# @Time    : 19-1-31
# @Author  : Zhiqi Kou
# @Email   : zhiqi1028@gmail.com

import requests
import pymysql
import json
import prettytable
from colorama import init, Fore, Back, Style


init(autoreset=False)


class Colored(object):

    #  前景色:红色  背景色:默认
    def red(self, s):
        return Fore.LIGHTRED_EX + s + Fore.RESET

    #  前景色:绿色  背景色:默认
    def green(self, s):
        return Fore.LIGHTGREEN_EX + s + Fore.RESET

    def yellow(self, s):
        return Fore.LIGHTYELLOW_EX + s + Fore.RESET

    def blue(self,s):
        return Fore.LIGHTBLUE_EX + s + Fore.RESET


class Tickets(object):
    """
    余票查询类
    """
    def __init__(self, train_date, from_station, to_station, purpose_codes='ADULT'):
        self.train_date = train_date
        self.from_station = from_station
        self.to_station = to_station
        self.purpose_codes = purpose_codes

    def get_url(self):
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="zhiqi",
            port=3306,
            database="fxxk12306",
            charset='utf8',
        )
        cursor = conn.cursor()
        get_from_code = """SELECT code FROM station_info WHERE name='%s'""" % self.from_station
        cursor.execute(get_from_code)
        from_code = cursor.fetchone()[0]
        get_to_code = """SELECT code FROM station_info WHERE name='%s'""" % self.to_station
        cursor.execute(get_to_code)
        to_code = cursor.fetchone()[0]

        # 关闭连接
        cursor.close()
        conn.close()

        url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?' \
                   'leftTicketDTO.train_date=' + self.train_date \
                   + '&leftTicketDTO.from_station=' + from_code \
                   + '&leftTicketDTO.to_station=' + to_code \
                   + '&purpose_codes=' + self.purpose_codes

        return url

    def search(self):
        try:
            r = requests.get(self.get_url(), timeout=30)
            r.raise_for_status()  # 如果状态不是200, 引发HTTPError异常
            r.encoding = r.apparent_encoding
        except:
            return "产生异常"

        # print(r.text)
        color = Colored()  # 创建Colored对象
        station_dict = json.loads(r.text)
        result = station_dict['data']['result']
        res_map = station_dict['data']['map']
        info_table = prettytable.PrettyTable(["日期", "车次", "出发站/到达站", "出发时间/到达时间",
                                  "历时", "商务座、特等座", "一等座", "二等座",
                                  "软卧", "硬卧", "硬座", "无座", "备注"])

        for info in result:
            info = info.split('|')
            # 显示列车详情
            from_station = res_map[info[6]]
            to_station = res_map[info[7]]

            if info[1] == '列车停运':
                # print('''【停止运行】出发时间:%s  车次:%s  出发站：%s 到达站:%s ''' %
                #       (self.train_date, info[3], from_station, to_station))
                info_table.add_row([self.train_date, color.yellow(info[3]), color.green(from_station) + "\n" + color.red(to_station),
                                     "-- \n --", '--', '--', '--', '--', '--', '--', '--', '--', '列车停运'])
                continue

            for i in range(len(info)):
                if info[i] == '':
                    info[i] = '--'
            info_table.add_row([self.train_date, color.yellow(info[3]), color.green(from_station) + "\n" + color.red(to_station),
                                color.green(info[8]) + "\n" + color.red(info[9]), color.blue(info[10]), info[32], info[31],
                                info[30], info[23], info[28], info[29], info[26], '-'])
            # print('''* 出发时间:%s  车次:%s  出发站：%s 到达站:%s  出发时间:%s 到达时间:%s  历时:%s''' %
            #       (self.train_date, info[3], from_station, to_station, info[8], info[9], info[10]))
            # print('''* 商务座、特等座:%s   一等座:%s   二等座:%s   软卧:%s   硬卧:%s   硬座:%s   无座:%s ''' %
            #       (info[32], info[31], info[30], info[23], info[28], info[29], info[26]))
        print(info_table)


if __name__ == '__main__':
    # 测试信息
    ticket = Tickets('2019-01-31', '洛阳', '北京')
    ticket.search()
