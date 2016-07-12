#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib
import urllib2
import cookielib


"""声明MozillaCookieJar对象实例保存cooke,之后写入文件"""
filename= 'cookie.txt'

"""登录网站信息"""
cookie= cookielib.MozillaCookieJar(filename)
opener= urllib2.builb_openner(urllib2.HTTPCookieProcessor(cookie))
postdata= urllib.urlencode({ 'name':'XXX','word':'XXX'})

"""网站url"""
loginurl= 'http://www.baidu.com'
"""模拟登陆"""
result= openner.open(loginurl,postdata)
"""保存cookie到cookie.txt文件中"""
cookie.save(ignore_discard=True,ignore_expires=True)

"""利用cookie登录同一域名下的其它子网址"""
sonurl= 'htttp://www.baidu.com/XXX/XXX'
""" 请求子网址"""
result= openner.open(sonrul)
print result.read()
