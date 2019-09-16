from Downloader import *

from MatchModel import *
import threading


class Spider:

     class crawer(threading.Thread):
          
          def __init__(self,url,name):
               
               threading.Thread.__init__(self)
               self.url=url
               self.name=name
               self.__initialize()

          def __initialize(self):
               
               content=Downloader.DownloadPageEx(self.url,charset='gb2312')
               self.image_list1=re.findall(COMMON_PICTURE_JPG,content)
               self.image_list2=re.findall(COMMON_PICTURE_PNG,content)

          def run(self):
               
               index=0
               for i in self.image_list1:
                    
                    
                    Downloader.DownloadSource(i,self.name+str(index)+".jpg")
                    index+=1

               for i in self.image_list2:
                    
                    Downloader.DownloadSource(i,self.name+str(index)+".png")
                    index+=1


     def __init__(self,root_url):
          '''intialize the compeoment of this spider'''

          self.root_url=root_url
          self.url_list=[]
          self.__initialize()       
     
     def __initialize(self):
          '''parser rooturl to url list'''

          card_p=r'<a href="/p/[0-9]*"'
          content=Downloader.DownloadPageEx(self.root_url,charset='gb2312')
          cards=re.findall(card_p,content)
          for card in cards:

               l=card.split("\"")
               self.url_list.append("https://tieba.baidu.com/"+l[1])

     def StartDownloading(self):

          index=0
          for url in self.url_list:

               temp=Spider.crawer(url,str(index))
               temp.start()
               index+=1

def Main():


     x=Spider("https://tieba.baidu.com/f?kw=%CE%B1%C4%EF&fr=ala0&tpl=5")
     x.StartDownloading()

Main()