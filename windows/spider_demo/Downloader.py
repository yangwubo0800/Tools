from urllib import *
from urllib import request

class Downloader:
    '''offer something function to get web information
    like http status or html source'''

    def __init__(self):
        '''meaningless'''
        
        pass


    @staticmethod
    def GetHttpStatus(url):
        '''get the http code of the url'''

        try:
            return request.urlopen(url).status

        except Exception as e:
            #occured something error

            print(e)
            #output the wrong information
            return None
        
        
    @staticmethod
    def DownloadPageEx(url,retry_times=3,user_agent="wswp",charset='gbk'):
        '''get the source of the html'''

        headers={'User-agent':user_agent}
        request_=request.Request(url,headers=headers)
        #set the user agent of the spilder

        
        if retry_times>0:
            print("downloading...",url)
            try:
                html=request.urlopen(url).read().decode(charset,'ignore')
                print("download sucessfully...")
            except Exception as e:

                print("download failed...")
                print(e)
                httpStatus=Downloader.GetHttpStatus(url)
                if httpStatus==None:
                    
                    print("perphaps the url is not exits...")
                elif httpStatus>=500:
                    #check the download error if belong to
                    #server error
                    
                    print("retry to download url...")
                    return DownloadPageEx(url,retry_times-1)
                
                elif httpStatus>=400:
                    #if the page is on error,then we can't move in
                    #or craw information from it
                    
                    print("the page is wrong...")
                html=None

            return html

    @staticmethod
    def CrawlSitemap(url):
        #download the sitemap file

        sitemap=Downloader.DownloadPageEx(url)
        print(sitemap)
        if sitemap==None:
            print("download failed...")
            return 
        #extract the sitemap links
        links=re.findall('<loc>(.*?)</loc>',sitemap)
        for link in links:

            html=WebInfo.DownloadPageEx(link)

    @staticmethod
    def DownloadSource(url,path):
        #download the source of url

        try:
            request.urlretrieve(url,path)
        except Exception as e:

            print("failed to download...")