#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Li Feilong <feiyang8068@qq.com>
"""

import json
import urllib
import urllib2
import random
from urllib2 import URLError, HTTPError


def get_json(text, sl, tl):

	headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0',
        'Referer': 'http://fanyi.baidu.com/'
    }

    url = 'http://fanyi.baidu.com/v2transapi'

    data = {'from': sl, 'query': text, 'simple_means_flag': 3, 'to': tl, 'transtype': 'trans'}

    request = urllib2.Request(url=url, headers=headers, data=data)
    try:
        response = urllib2.urlopen(request)
    except HTTPError, e:
        print e.code
    except URLError, e:
        print e.reason
    else:
        ret = response.read().decode('utf-8')
        jd = json.loads(ret)
        print jd


if __name__ == '__main__':
    print get_json('Chinese Culture', 'en', 'zh')

