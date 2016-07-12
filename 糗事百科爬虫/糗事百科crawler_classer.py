#! /usr/bin/env python
# -*- coding: utf-8 -*-


import urllib
import urllib2
import re


"""糗事百科的爬虫类"""
class QSBK:
    def __init__(self):
        self.pageIndex= 1
        self.user_agent= 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
        self.headers= {'User-Agent': self.user_agent,'Referer':\
                       'http://www.qiushibaike.com/hot/'}                        
        self.stories= []
        self.enable= False

    #传入某一页索引获得页面代码
    def getpage(self,pageIndex):
        try:
            url= 'http://www.qiushibaike.com/hot/page/'+ str(pageIndex)
            request= urllib2.Request(url,headers= self.headers)
            response= urllib2.urlopen(request)
            pagecode= response.read().decode('utf-8')
            return pagecode
        except urllib2.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
                return None
            if hasattr (e,"reason"):
                print u"连接糗事百科失败，错误原因",e.reason
                return None

    #传入某页代码，返回本页不带图片的段子列表
    def getpageItems (self,pageIndex):
        pageCode= self.getpage(pageIndex)
        if not pageCode:
            print (u"页面加载失败...")
            return None
        pattern= re.compile(r'<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?'+
                            r'content">(.*?)</div>(.*?)<div class="stats.*?class='+
                            r'"number">(.*?)</i>',re.S)
        items= re.findall(pattern,pageCode)
        pageStories= []
        for item in items:
            haveImg= re.search("img",item[2])
            if not haveImg:
                replaceBR= re.compile('<br/>')
                text= re.sub(replaceBR,"\n",item[1])
                pageStories.append({'author':item[0].strip(),'context':text.strip(),\
                                    'agerrcount':item[3].strip()})
        return pageStories

    #加载并提取页面的内容，加入到列表中
    def loadpage(self):
        if self.enable== True:
                pageStories= self.getpageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex+= 1

    #调用该方法，每次回车键打印输出一个段子
    def getOneStory(self,pageStories,page):
        for story in pageStories:
            input= raw_input()
            if input== "Q":
                self.enable= False
                return
            print u"第%d页\t发布人:%s\t赞:%s\n%s" %(page,story['author'],story['agerrcount'],\
                                                    story['context'])
        self.loadpage()

    #开始方法
    def start(self):
        print (u"正在读取糗事百科，按回车查看新段子，Q退出")
        self.enable= True
        self.loadpage()
        nowpage= 0
        while self.enable:
            if len(self.stories)>0:
                pageStories= self.stories[0]
                nowpage += 1
                del self.stories[0]
                self.getOneStory(pageStories,nowpage)


spider= QSBK()
spider.start()
                    
                                   
        

    
        
