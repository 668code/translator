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
        'Referer': 'http://fanyi.youdao.com/',
    }

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

    trans_type = 'EN2ZH_CN'
    data = {'type': trans_type, 'i': text, 'doctype': 'json', 'xmlVersion': '1.8', 'keyfrom': 'fanyi.web', 'action': 'FY_BY_CLICKBUTTON', 'typoResult': 'true'}
    data = urllib.urlencode(data)
    request = urllib2.Request(url=url, data=data, headers=headers)
    try:
        response = urllib2.urlopen(request)
        ret = response.read().decode('utf-8')
        print ret
        jd = json.loads(ret)
        print jd
        return jd['translateResult']
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
        ret += '%s' % item[0]['tgt']
    return ret


if __name__ == '__main__':
    # get_json('Chinese Culture\nHello', 'en', 'zh')
    # print get_json('Chinese Culture\nHello', 'en', 'zh')
    print translate_simple('Chinese Culture\nHello', 'en', 'zh')


