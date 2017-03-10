#encoding:utf-8

__author__ = 'yinchuandong'

import urllib2
import urllib
from bs4 import BeautifulSoup
import base64
import json


def getSchoolList():
    jsonStr = urllib2.urlopen("http://api.superlib.cn/index.php/Api/School/getSchoolList").read()
    jsonObj = json.loads(jsonStr)
    # jsonObj = json.JSONDecoder().decode(jsonStr)
    print jsonObj['data']['School'][0]['schoolName']
    return

def getQueryInfo():
    params = {
        "sfz_h": "500382199307154136",
        "xm": "尹川东".decode("utf-8", "ignore").encode("gb2312"),
        "bynf": "2015",
        "Submit": "查询我的档案去向"
    }

    url = "http://www.gradjob.com.cn/defaults/bsdt/dacx_sn.jsp"
    data = urllib.urlencode(params)
    print "data:", data

    content = urllib2.urlopen(url, data).read()
    content = content.decode('gb2312')
    doc = BeautifulSoup(content)
    result = doc.find('form', attrs={"name":"frm"}).find('p', attrs={"style":True})
    print result
    print doc.find('title').string



    return

if __name__ == '__main__':
    #getSchoolList()
    getQueryInfo()