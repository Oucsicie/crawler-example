#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib
import urllib2
import cookielib


"""设置头文件爬虫"""
url= 'http://baidu.com'
user_agent= 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
values= {'username':'XXX','password':'XXX'}
headers= {'User-Agent':user_agent,'Referer':'http://baidu.com/XXX'}

data= urllib.urlencode(values)
request= urllib2.Request(url,data,headers)
response= urllib2.urlopen(request)
page= response.read()


"""设置代理"""
enable_proxy=True
proxy_handler= urllib2.ProxyHandler({"http":'http://some-proxy.com:8080'})
null_proxy_handler= urllib2.ProxyHandler({})

if enable_proxy:
    opener= urllib2.bulib_opener(proxy_handler)
else:
    opener= urllib2.bulib_opener(null_proxy_handler)
urllib2.install_opener(opener)


"""使用urllib2发出PUT或DELETE方法"""
request=urllib2.Request(url,data=data)
request.get_method= lambda:'PUT' #or 'DELETE'
reponse= urllib2.urlopen(request)


"""打开Debuglog,在屏幕上显示收发包"""
httpHandler= urllib2.HTTPHandler(dabuglevel=1)
httpsHandler= urllib2.HTTPSHandler(debuglevel=1)
opener=urllib2.bulib_opener(httpHandler,httpsHandler)
urllib2.install_opener(opener)
response= urllib2.urlopen('http;//www.baidu.com')


"""异常处理两种写法"""
#父类错误捕捉放在子类错误捕捉后面
req= urllib2.request('http://www.baidu.com')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError,e:
    print e.code
except urllib2.URLError,e:
    print e.reason
else:
    print "ok"

#使用hasattr属性判断
req=urllib2.request('http://www.baidu.com')
try:
    urllib2.urlopen(req)
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
else:
    print "OK"


"""cokkie用法"""
#保存到变量
cookie= cookielib.CookieJar()
handler= urllib2.HTTPCookieProcessor(cookie)
opener= urllib2.build_opener(hanler)
response= opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name= '+item.name
    print 'Value= '+ item.value

#保存到文件
filename= 'cookie.txt'
cookie= cookielib.MozillaCookieJar(filename)
handler= urllib2.HTTPCookieProcessor(cookie)
opener= urllib2.build_opener(handler)
response= opener.open("http://www.baidu.com")
cookie.save(ignore_discard= True,ignore_expires= True)

#文件获取cookie访问
cookie= cookielib.MozillaCookiejar()
cookie.load('cookie.txt',ignore_discard= True,ignore_expires= True)
req= urllib2.Request("http://www.baidu.com")
opener= urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response= opener.open(req)
print response.read()

#利用cookie模拟登陆
filename='cookie.txt'
cookie= cookielib.MozillaCookieJar(filename)
opener= urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata= urllib.urlencode({'XXX':'XXX','XXX':'XXX'})
loginUrl= 'http://xxx.xxx.cn:7036/xxx/xxx'
result= opener.open(loginUrl,postdata)
cookie.save(ignore_discard=Ture,ignore_expires=Trure)
anotherUrl= 'http://........'
result= opener.open(anotherUrl)
print result.read()




