#! usr/bin/env python
# -*- coding:utf-8 -*-


import urllib
import urllib2
import re
from handle import Tool


"""处理页面标签类"""
"""class Tool:
    removeImg= re.compile('<img.*?>| {7}|')
    removeAddr= re.compile('<a.*?>|</a>')
    replaceLine= re.compile('<tr>|<div>|</div>|</p>')
    replaceTD= re.compile('<td>')
    replacePara= re.compile('<p.*?>')
    replaceBR= re.compile('<br><br>|<br>')
    removeExtraTag= re.compile('<.*?>')

    def replace(self,x):
        x= re.sub(self.removeImg,"",x)
        x= re.sub(self.removeAddr,"",x)
        x= re.sub(self.replaceLine,"\n",x)
        x= re.sub(self.replaceTD,"\t",x)
        x= re.sub(self.replacePara,"\n    ",x)
        x= re.sub(self.replaceBR,"\n",x)
        x= re.sub(self.removeExtraTag,"",x)
        return x.strip()"""


"""百度贴吧爬虫类"""
class BDTB:
    def __init__(self,baseurl,seeLZ,floorTag):
        self.baseURL= baseurl
        self.seeLZ= '?see_lz='+str(seeLZ)
        self.tool= Tool()
        self.file=None
        self.floor=1
        self.defaultTitle= u"百度贴吧"
        self.floorTag= floorTag 

    #传入页码，获取该页面帖子的内容
    def getPage(self,pageNum):
        try:
            url= self.baseURL+ self.seeLZ+ '&pn='+str(pageNum)
            request= urllib2.Request(url)
            response= urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError as e:
            if hasattr(e,"code"):
                print e.code
                return None
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败，错误原因",e.reason
                return None

    #提取标题
    def getTitle(self,page):
        pattern= re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        result= re.search(pattern,page)
        if result:
            #print result.group(1) #测试输出
            return result.group(1).strip()
        else:
            return None

    #提取总页数
    def getPageNum(self,page):
        pattern= re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>'+
                            '(.*?)</span>',re.S)
        result= re.search(pattern,page)
        if result:
            #print result.group(1) #测试输出
            return result.group(1).strip()
        else:
            return None

    #获取每一层楼的内容，传入页面的内容
    def getContent(self,page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        contents=[]
        for item in items:
            content="\n"+self.tool.replace(item)+"\n"
            contents.append(content.encode('utf-8'))
        return contents
    
    #设置文件名
    def setFileTitle(self,title):
        if title is not None:
            self.file= open(title+ ".txt","w+")
        else:
            self.file= open(self.defaultTitle+ ".txt","w+")

    #把内容写入文件
    def writeData(self,contents):
        for item in contents:
            if self.floorTag== '1':
                floorLine= "\n"+ str(self.floor)+ u"---------------------------\
----------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor+= 1
            
    #整合程序
    def start(self):
        indexPage= self.getPage(1)
        pageNum= self.getPageNum(indexPage)
        title= self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum== None:
            print u"URL已失效，请重试"
            return
        try:
            print u"该帖子共有" + str(pageNum) + u"页"
            for i in range(1,int(pageNum)+1):
                print u"正在写入弟" + str(i) + u"页数据"
                page= self.getPage(i)
                contents= self.getContent(page)
                self.writeData(contents)
        except IOError as e:
            print u"写入异常，原因" + e.massage
        finally:
            print u"写入任务完成"


print u"请输入帖子代号"
baseURL= 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
seeLZ= raw_input("是否只获取楼主发言，是输入1，否输入0\n")
floorTag= raw_input("是否写入楼层信息，是输入1，否输入0\n")
bdtb= BDTB(baseURL,seeLZ,floorTag)
bdtb.start()
        


