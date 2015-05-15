#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Li Feilong <feiyang8068@qq.com>
"""

import json
import urllib
import urllib2
from urllib2 import URLError, HTTPError


def get_json(text, sl, tl):
    """
    :param text:
    :param sl: source language
    :param tl: target language
    :return:
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0',
        'Referer': 'http://fanyi.baidu.com/',
    }

    url = 'http://fanyi.baidu.com/v2transapi'

    data = {'from': sl, 'query': text, 'simple_means_flag': 3, 'to': tl, 'transtype': 'trans'}
    data = urllib.urlencode(data)
    request = urllib2.Request(url=url, data=data, headers=headers)
    try:
        response = urllib2.urlopen(request)
        ret = response.read().decode('utf-8')
        jd = json.loads(ret)
        return jd['trans_result']['data']
    except HTTPError, e:
        print e.code
    except URLError, e:
        print e.reason


def translate_simple(word, sl, tl):
    """
    Simple translate
    :param word:
    :param sl:
    :param tl:
    :return:
    """
    jd = get_json(word, sl, tl)
    ret = ''
    for item in jd:
        ret += '%s' % item['dst']
    return ret


if __name__ == '__main__':
    # print get_json('Chinese Culture\nHello', 'en', 'zh')
    print translate_simple('Chinese Culture\nHello', 'en', 'zh')
