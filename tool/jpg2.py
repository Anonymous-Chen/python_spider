
from HTMLParser import HTMLParser  
from re import sub  
from sys import stderr  
from traceback import print_exc  
import urllib2
import re
import urlparse
from bs4 import BeautifulSoup

   
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
    
    for i in range(2, 3):
        u = "http://1024.luj8le.biz/pw/thread.php?fid=15&page=" + str( i )
        u_2(u)

        




def u_2(url):
    
    count = 1
    
    request = urllib2.Request(url)
    request.add_header("user-agent", "Mozilla/5.0")
    response2 = urllib2.urlopen(request)
    read = response2.read()
    soup = BeautifulSoup(read, 'html.parser', from_encoding='utf-8')
    links = soup.find_all('a', href=re.compile(r"htm_data/15/\w+"))
    for link in links:
        new_url = link['href']
        new_full_url = urlparse.urljoin(url, new_url)
        u_3(new_full_url,count)
        
        count = count+1
    


def u_3(url,count):
    

    try:
         
        request = urllib2.Request(url)
        request.add_header("user-agent", "Mozilla/5.0")
        response2 = urllib2.urlopen(request)   
                      
        soup = BeautifulSoup(response2.read(), 'html.parser', from_encoding='utf-8')
        link1 = soup.find('th', id="td_tpc")
        link2 = link1.find('h1', id="subject_tpc")
        link3s = soup.find_all('img', src=re.compile(r"http://33img.com/upload/image/\w+"))  
            
        count1 = 0
        for link3 in link3s:
                
            count1 = count1 + 1
            title = link2.get_text()+str(count1)+'.jpg'
                
            print title
            imgurl = link3['src'] + "?imageView2/0/w/640"
               
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
                'Cookie': 'AspxAutoDetectCookieSupport=1',
            }
            request = urllib2.Request(imgurl, None, header)
                
            response = urllib2.urlopen(request)
                
            x = response.read()

            f = open(title , 'wb')
            f.write( x )
            f.close()
                
            print count,title
            
    except:
        print 'craw failed'   
            
            
        
def main():

    u_1()
    print 'end'
  
   
if __name__ == '__main__':  
    main()