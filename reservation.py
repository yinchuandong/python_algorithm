#encoding:utf-8

import os
import threading
import time

import urllib2
import urllib
import cookielib
from bs4 import BeautifulSoup
import base64
import json

class Reservation(object):
    name = ''
    password = ''
    cookie = None
    cookieFile = './cookies.dat'
    isLogin = False

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.cookie = cookielib.LWPCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib2.install_opener(opener)

    def login(self):
        params = {
            "name": self.name,
            "password": self.password
        }

        url = "http://203.91.43.52:8097/wsyy/sysManager/user/login.action"
        data = urllib.urlencode(params)
        # print "data:", data

        content = urllib2.urlopen(url, data).read()
        # print content
        # content = content.decode('gb2312')
        doc = BeautifulSoup(content)
        form_id = doc.find('input', attrs={"name":"id"}).attrs['value']
        print form_id

        # ----- second form submit ---- 
        params = {
            'name': self.name,
            'id': form_id
        }

        url2 = "http://203.91.43.52:8097/wsyy/sysManager/user/user!login.action"
        data = urllib.urlencode(params)
        content = urllib2.urlopen(url2, data).read()
        doc = BeautifulSoup(content)
        namestr = doc.find('font', attrs={'color': 'red'}).string
        if namestr == u"尹川东":
            isLogin = True
            print 'success login'

        self.cookie.save(self.cookieFile)

        # print content

        # info = urllib2.urlopen("http://203.91.43.52:8097/wsyy/sysManager/yygl/yygl!userInfo.action").read()
        # print info
        # 
        return
    
    def reserve(self, timeKey, day="2015-08-21"):

        url = "http://203.91.43.52:8097/wsyy/sysManager/yygl/yygl!saveWsyy.action?wherecome=1"
        periodArr = [
            "09:00-10:00",
            "10:00-11:00",
            "11:00-12:00",
            "14:00-15:00",
            "15:00-16:00",
            "16:00-17:00",
            "17:00-18:00"
        ]

        print periodArr[timeKey - 1]

        params = {
            "timeList": periodArr[timeKey - 1],
            "timeKey": timeKey, 
            "deptId": "440305580000",
            "deptName": "高新技术园区派出所",
            "bussionId": "33",
            "bussionName": "毕业生入户（不需本市准迁）",
            "yyTime": day,
            "yyPersonType": "",
            "otherPersonId": "",
            "wherecome": "1"
        }

        data = urllib.urlencode(params)
        # print data
        # print urllib.unquote(data)
        content = urllib2.urlopen(url, data).read()
        content = str(content)

        if '您选择的日期时间段内预约人数已满' not in content:
            # successfully reserve
            # os.system('say 预约成功啦')
            print 'true'
        else:
            print 'false'
            # os.system('say 预约失败')
            # print content
        return

    def run(self, day="2015-08-21"):
        for i in range(6):
            try:
                self.reserve(timeKey=(i + 1), day=day)
            except Exception, e:
                print 'exception in line 121'
                # raise e 
        return


class Timer(threading.Thread):
    def __init__(self, day):
        threading.Thread.__init__(self)
        self.day = day
        self.isStopped = False
        # self.setDaemon(True)

    def run(self):
        model = Reservation('13620988145', '***')
        model.login()
        while not self.isStopped:
            model.run(day=self.day)
            # time.sleep(1)
        return

    def stop(self):
        self.isStopped = True
        return



#--------------------
#

def singleMain():
    model = Reservation('13620988145', '***')
    model.login()
    while 1:
        model.run(day="2015-08-22")
    return

def multiMain():
    dayArr = [
        "2015-08-03",
        "2015-08-04"
        "2015-08-05",
        "2015-08-07",
        "2015-08-08"

        "2015-08-10",
        "2015-08-11"
        "2015-08-12",
        "2015-08-13",
        "2015-08-14"
        "2015-08-15",

        "2015-08-17",
        "2015-08-18"
        "2015-08-19",
        "2015-08-20",
        "2015-08-21"
    ]

    threadArr = []
    for i in range(len(dayArr)):
        thread = Timer(dayArr[i])
        threadArr.append(thread)
        thread.setDaemon(True)
        thread.start()

    while 1:
        alive = False
        if i in range(len(threadArr)):
            alive = alive or threadArr[i].isAlive

        if not alive:
            break
    return


if __name__ == '__main__':
    # singleMain()
    # multiMain()

    








