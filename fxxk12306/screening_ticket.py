# @Time    : 19-1-31
# @Author  : Zhiqi Kou
# @Email   : zhiqi1028@gmail.com

from search_tickets import Tickets


class TargetTicket(object):
    def __init__(self, trains):
        self.trains = trains

    def screening_trains(self, all_tickets):
        # 得到指定车次信息
        target_dir = {}
        for ticket in all_tickets:
            if ticket['trains'] in self.trains:
                seat_dir = {}
                if ticket['tdz'] != '--':
                    seat_dir['tdz'] = ticket['tdz']
                if ticket['ydz'] != '--':
                    seat_dir['ydz'] = ticket['ydz']
                if ticket['edz'] != '--':
                    seat_dir['edz'] = ticket['edz']
                if ticket['gjrw'] != '--':
                    seat_dir['gjrw'] = ticket['gjrw']
                if ticket['rw'] != '--':
                    seat_dir['rw'] = ticket['rw']
                if ticket['yw'] != '--':
                    seat_dir['yw'] = ticket['yw']
                if ticket['yz'] != '--':
                    seat_dir['yz'] = ticket['yz']
                if ticket['wz'] != '--':
                    seat_dir['wz'] = ticket['wz']
                target_dir[ticket['trains']] = seat_dir
        print(target_dir)
        return target_dir

    def screening_seat(self, all_tickets, trains_seat_dir):
        target_dir = self.screening_trains(all_tickets)
        for key in trains_seat_dir:
            print(key)
            for seat in trains_seat_dir[key]:
                print(target_dir[key][seat])


if __name__ == '__main__':
    # 测试信息
    tickets = Tickets('2019-03-01', '上海', '北京')
    # 打印所有车票信息
    print(tickets)
    # 得到所有车票列表
    all_tickets = tickets.search()
    # 晒选指定车次
    target_ticket = TargetTicket(['D708', 'Z282', 'G22'])
    # target_ticket.screening_trains(all_tickets)
    target_ticket.screening_seat(all_tickets, {'D708': ['edz', 'rw'], 'Z282': ['rw', 'wz']})
