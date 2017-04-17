
from HTMLParser import HTMLParser  
from re import sub  
from sys import stderr  
from traceback import print_exc  
import urllib2
import cookielib
import re
import urlparse
from bs4 import BeautifulSoup
import os, sys
   
class _DeHTMLParser(HTMLParser):  
    def __init__(self):  
        HTMLParser.__init__(self)  
        self.__text = []  
   
    def handle_data(self, data):  
        text = data.strip()  
        if len(text) > 0:  
            text = sub('[ \t\r\n]+', ' ', text)  
            self.__text.append(text + ' ')  
   
    def handle_starttag(self, tag, attrs):  
        if tag == 'p':  
            self.__text.append('\n\n')  
        elif tag == 'br':  
            self.__text.append('\n')  
   
    def handle_startendtag(self, tag, attrs):  
        if tag == 'br':  
            self.__text.append('\n\n')  
   
    def text(self):  
        return ''.join(self.__text).strip()  
   
   
def dehtml(text):  
    try:  
        parser = _DeHTMLParser()  
        parser.feed(text)  
        parser.close()  
        return parser.text()  
    except:  
        print_exc(file=stderr)  
        return text  
   
   
def u_1():
    urls = set()
    for i in range(10, 20):
        u = "http://1024.luj8le.biz/pw/thread.php?fid=17&page=" + str( i )
        urls.add(u)
    
    print urls
    return urls
        


def u_2(urls):
    urls_a = set()

    for url in urls:
        request = urllib2.Request(url)
        request.add_header("user-agent", "Mozilla/5.0")
        response2 = urllib2.urlopen(request)
        read = response2.read()
        soup = BeautifulSoup(read, 'html.parser', from_encoding='utf-8')
        links = soup.find_all('a', href=re.compile(r"htm_data/17/\w+"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url, new_url)
            urls_a.add(new_full_url)
    

    return urls_a


def u_3(urls_a,urls_h):
    
    count = 1
    urls_a = urls_a-urls_h

    print '1'
    
    for url in urls_a:
        
        fout = open('txt_urls.txt' , 'a')
        fout.write( url+'\n' )
        fout.close()
        
        try :
            request = urllib2.Request(url)
            request.add_header("user-agent", "Mozilla/5.0")
            response2 = urllib2.urlopen(request)   
            soup = BeautifulSoup(response2.read(), 'html.parser', from_encoding='utf-8')
            link1 = soup.find('th', id="td_tpc")   
            link2 = link1.find('h1', id="subject_tpc")
            title = link2.get_text()+'.txt'
            read = dehtml(str(link1))
            
            print count
            
            fout1 = open( "stxt/"+title , 'w')
            fout1.write( read )
            fout1.close()
            count = count+1
            
        except:
            print 'craw failed'
        
def main():
    
    urls_h = set()
    file_object = open('txt_urls.txt')
    try:
        for line in file_object:
            urls_h.add(line[:-1]) 
    finally:
        file_object.close( )
        
    path = "stxt"
    
    if (os.path.exists(path)):
        pass
    else:
        os.mkdir( path );
    
    
    
    urls = u_1()
    urls_a = u_2(urls)
    u_3(urls_a,urls_h)
    
    print 'end'
   
if __name__ == '__main__':  
    main()