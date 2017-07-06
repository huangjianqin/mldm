# -*- coding: utf-8 -*-
import itchat
from echarts import Echart, Pie, Legend

if __name__ == '__main__':
    itchat.login()
    # 第一个是自己的账号信息
    friends = itchat.get_friends(update=True)

    male = female = other = 0

    for i in friends[1:]:
        sex = i["Sex"]
        if sex == 1:
            male += 1
        elif sex == 2:
            female +=1
        else:
            other += 1

    total = len(friends[1:])

    print "男性好友占比例:%.4f%% (%d)" % ((float(male) / total) * 100, male)
    print "女性好友占比例:%.4f%% (%d)" % ((float(female) / total) * 100, female)
    print "其他性别好友占比例:%.4f%% (%d)" % ((float(other) / total) * 100, other)

    itchat.logout()

    chart = Echart(u'%s的微信好友性别比例' % (friends[0]['NickName']), 'from WeChat')
    chart.use(Pie('WeChat',
                  [{'value': male, 'name': u'男性 %.4f%%' % (float(male) / total * 100)},
                   {'value': female, 'name': u'女性 %.4f%%' % (float(female) / total * 100)},
                   {'value': other, 'name': u'其他 %.4f%%' % (float(other) / total * 100)}],
                  radius=["50%", "70%"]))
    chart.use(Legend(["male", "female", "other"]))
    del chart.json["xAxis"]
    del chart.json["yAxis"]
    chart.plot()