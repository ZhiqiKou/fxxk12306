# @Time    : 19-1-31
# @Author  : Zhiqi Kou
# @Email   : zhiqi1028@gmail.com

from search_tickets import Tickets


class TargetTicket(object):
    def __init__(self, trains):
        self.trains = trains

    def screening_trains(self, all_tickets):
        """
        得到指定车次信息
        :param all_tickets: 所选日期内所有列车
        :return: 目标车次的余票信息
        """
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
        """
        筛选车次车票
        :param all_tickets: 所选日期内所有列车
        :param trains_seat_dir: 想要购买的车次和席位
        :return: 有余票的车次和席位
        """
        target_dir = self.screening_trains(all_tickets)
        for key in trains_seat_dir:
            print(key)
            for seat in trains_seat_dir[key]:
                print(target_dir[key][seat])
                tickets_num = target_dir[key][seat]
                if tickets_num != '无':
                    # 购买车票
                    print('购买{0}车次，{1}车票'.format(key, seat))
                    # 结束循环
                    return key, seat


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
