# @Time    : 19-1-31
# @Author  : Zhiqi Kou
# @Email   : zhiqi1028@gmail.com

from search_tickets import Tickets


class TargetTicket(object):
    def __init__(self, trains, train_date, from_station, to_station, purpose_codes='ADULT'):
        self.trains = trains
        self.train_date = train_date
        self.from_station = from_station
        self.to_station = to_station
        self.purpose_codes = purpose_codes

    def screening(self):
        tickets = Tickets(self.train_date, self.from_station, self.to_station)
        # 得到所有车票
        all_tickets = tickets.search()
        # 得到指定车票信息
        target_list = []
        for ticket in all_tickets:
            if ticket['trains'] == self.trains:
                target_list.append(ticket)
        print(target_list)


if __name__ == '__main__':
    # 测试信息
    target_ticket = TargetTicket('K270', '2019-02-01', '洛阳', '北京')
    target_ticket.screening()
