#coding:utf-8

import urllib
import urllib2
from lxml import etree

def loadpage(url):
    #根据url发送请求,获取服务器响应文件
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"}
    request = urllib2.Request(url,headers=headers)
    html =urllib2.urlopen(request).read()
    # 解析HTML文档为HTML DOM模型
    content= etree.HTML(html)
    link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')

    for link in link_list:
        fulllink = "http://tieba.baidu.com" + link
        loadImage(fulllink)

# 取出每个帖子里的每个图片链接
def loadImage(link):
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"}
    request = urllib2.Request(link,headers=headers)
    html = urllib2.urlopen(request).read()
    content = etree.HTML(html)
    link_list = content.xpath('//div[@class="post_bubble_middle"]')
    for link in link_list:
        print 'loadmage link'
        print link

def writeImage(link):
    #将html内容写入到本地
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"}
    request = urllib2.Request(link,headers=headers)
    image = urllib2.urlopen(request).read()
    filename = link[-10:]
    with open(filename,'wb') as f:
        f.write(image)
    print '已经成功下载'+filename

def tiebaSpider(url,beginPage,endPage):
    for page in range(beginPage,endPage + 1):
        pn = (page -1)*50
        fullurl = url + "&pn=" + str(pn)
        loadpage(fullurl)

        print '谢谢使用'

if __name__ == '__main__':
    kw = raw_input("请输入需要爬去的贴吧名:")
    beginPage = int(raw_input("请输入起始页码:"))
    endPage= int(raw_input("请输入结束页码:"))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    fullurl = url + key
    print "fullurl"
    print fullurl
    tiebaSpider(fullurl, beginPage, endPage)

