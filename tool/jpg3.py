import urllib2
import re
import urlparse
from bs4 import BeautifulSoup
import os, sys

   
   
def u_1():
    urls = set()
    for i in range(2, 3):
        u = "http://1024.luj8le.biz/pw/thread.php?fid=14&page=" + str( i )
        urls.add(u)
    return urls
        




def u_2(urls):
    urls_a = set()
    print '1'
    for url in urls:
        request = urllib2.Request(url)
        request.add_header("user-agent", "Mozilla/5.0")
        response2 = urllib2.urlopen(request)
        read = response2.read()
        soup = BeautifulSoup(read, 'html.parser', from_encoding='utf-8')
        links = soup.find_all('a', href=re.compile(r"htm_data/14/\w+"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url, new_url)
            urls_a.add(new_full_url)
    
    return urls_a




def u_3(urls_a,urls_h):
    print '2'
    count = 1
    urls_a = urls_a-urls_h

    
    for url in urls_a:
        
        fout = open('jpg_urls2.txt' , 'a')
        fout.write( url+'\n' )
        fout.close()

        try:
            count = count+1
            
            request = urllib2.Request(url)
            request.add_header("user-agent", "Mozilla/5.0")
            response2 = urllib2.urlopen(request,timeout=10)   
                      
            soup = BeautifulSoup(response2.read(), 'html.parser', from_encoding='utf-8')
            link1 = soup.find('th', id="td_tpc")
            link2 = link1.find('h1', id="subject_tpc")
            link3s = soup.find_all('img', src=re.compile(r"http://33img.com/upload/image/\w+"))  
            
            count1 = 0
            
            print '3'
            
            print link3s
            for link3 in link3s:
                
                try:
                
                    count1 = count1 + 1
                    title = link2.get_text()+str(count1)+'.jpg'
                    
                    path = "sjpg/"+link2.get_text()
        
                    if (os.path.exists(path)):
                        pass
                    else:
                        os.mkdir( path );
                    
    #                 imgurl = link3['src'] + "?imageView2/0/w/640"
                    imgurl = link3['src']
                   
                    header = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
                        'Cookie': 'AspxAutoDetectCookieSupport=1',
                    }
                    
                    print imgurl 

                    request = urllib2.Request(imgurl)
                    request.add_header("user-agent", "Mozilla/5.0")
                    response = urllib2.urlopen(request ,timeout=10)   
                    
                    print '3'
                    x = response.read()
                    print '3'
    
                    f = open(path+"/" +title , 'wb')
                    f.write( x )
                    f.close()
                    
                    print count,count1,imgurl
                except:
                    print 'craw failed1'
            
        except:
            print 'craw failed2' 
    
    


            
            
        
def main():

    urls_h = set()
    file_object = open('jpg_urls2.txt')
    try:
        for line in file_object:
            urls_h.add(line[:-1]) 
    finally:
        file_object.close( )
        
    path = "sjpg"
    
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