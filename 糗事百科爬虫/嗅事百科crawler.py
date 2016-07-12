#! /usr/bin/env python
# -*- coding: utf-8 -*-


import urllib
import urllib2
import re


"""抓取糗事百科热门第一页全部HTML数据"""
page=1
url= 'http://www.qiushibaike.com/hot/page/'+str(page)
user_agent= 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers= {'User-Agent': user_agent, 'Referer':'http://www.qiushibaike.com/hot/'}

try:
    request= urllib2.Request(url,headers= headers)
    response= urllib2.urlopen(request)
except urllib2.URLError as e:
    if hasattr(e,"code"):
        print (e.code)
    if hasattr(e,"reason"):
        print (e.reason)
        
"""正则表达式抓取内容，去除带有不便显示的图片内容的文章"""        
content= response.read().decode('utf-8')
pattern= re.compile(r'<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?'+
                    r'content">(.*?)</div>(.*?)<div class="stats.*?class='+
                    r'"number">(.*?)</i>',re.S)
items= re.findall(pattern,content)
for item in items:
    haveImg= re.search("img",item[2])
    if not haveImg:
        print item[0],item[1],item[3]
    


