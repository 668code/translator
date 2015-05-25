#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Li Feilong <feiyang8068@qq.com>
Translate content use google service.
tk list:
'519542|900545', '519539|805995', '519602|872956', '520745|107443', '519224|907827', '519555|922865',
'520898|133019', '521042|136276', '521045|784331', '521073|523001', '520967|447515', '520986|658935',
'520226|467348'
"""

import re
import json
import urllib
import urllib2
import random
from urllib2 import URLError, HTTPError

JSON_PINYIN_KEY = 99999999


def get_json(text, sl, tl):
    """
    tk value: '519542|900545'
    :param text: string
    :param sl: source language
    :param tl: target language
    :return: json
    """
    sl = 'zh-CN' if sl == 'cn' else sl
    sl = 'zh-TW' if sl == 'tw' else sl

    tl = 'zh-CN' if tl == 'cn' else tl
    tl = 'zh-TW' if tl == 'tw' else tl

    service_url = 'http://translate.google.com/'
    text = urllib.quote(str(text.encode('utf-8')))
    tk = '519542|900545'
    url = 'translate_a/single?client=t&sl=%s&tl=%s&hl=en&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&oe=UTF-8&source=btn&srcrom=0&kc=0&ssel=3&tsel=6&tk=%s&q=%s' % (sl, tl, tk, text)
    url = '%s%s' % (service_url, url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0',
        'Referer': service_url
    }
    
    request = urllib2.Request(url=url, headers=headers)
    try:
        response = urllib2.urlopen(request)
    except HTTPError, e:
        print e.code
    except URLError, e:
        print e.reason
    else:
        ret = response.read().decode('utf-8')
        cleanup = re.subn(r',(?=,)', '', ret)[0]
        json_ret = json.loads(cleanup.replace(r'\xA0', r' ').replace('[,', '[%s,' % JSON_PINYIN_KEY), encoding='UTF-8')
        # print json_ret[0]
        return json_ret[0]


def translate_simple(word, sl, tl):
    """
    简单单词翻译
    :param word:
    :param sl:
    :param tl:
    :return:
    """
    jd = get_json(word, sl, tl)

    ret = ''
    for item in jd:
        if item[0] != JSON_PINYIN_KEY:
            ret += '%s' % item[0]
    return ret


if __name__ == '__main__':
    #print get_json('Chinese Culture', 'en', 'cn')
    print translate_simple('Chinese Culture', 'en', 'cn')
