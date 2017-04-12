#coding=utf-8

#从百度贴吧下载图片
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(http://33img.com/upload/image/.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 1
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
    

html = getHtml("https://tieba.baidu.com/p/2460150866")

getImg(html)

