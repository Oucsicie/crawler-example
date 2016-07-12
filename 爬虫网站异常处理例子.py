#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib2


req= urllib2.Request('http://www.baidu.com')

try:
    urllib2.urlopen(req)
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print(e.code)
except urllib2.URLError,e:
    if hasattr(e,"reason"):
        print(e.reason)
else:
    print("OK")
