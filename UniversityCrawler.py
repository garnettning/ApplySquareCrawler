# -*- coding: UTF-8 -*-

from Crawler import url2str,start
import bs4
def LinkList(UniversityUrl):
    htmlstr = url2str(UniversityUrl)
    soup = bs4.BeautifulSoup(htmlstr)
    html = soup.html

    listall = html.findAll(lambda tag:tag.name=='a' and tag.attrs.has_key('class') and tag.attrs['class'][0]=='clickable')
    LinkList=[]
    for i in listall:
        link = 'https://www.applysquare.com'+i.attrs['href'].encode("utf-8")
        LinkList.append(link)
    return LinkList

def UniversityStart(UniversityUrl):
    List = LinkList(UniversityUrl)
    print '***************************************************************'
    print '*******      University - All program -Mysql      *************'
    print '***************************************************************'
    print 'There are %d links'%len(List)
    print 'Start!'
    FailedUrllist=[]
    x=0
    for i in List:
        x+=1
        print '\n******* No.%d ******'%x
        print 'Link = '+i
        print 'Hard Working...'
        flag = start(i)
        if flag:
            print 'Success!'
        else:
            print 'Failure'
            FailedUrllist.append(i)
            
    if FailedUrllist:
        print 'failed link num: %d'%len(FailedUrllist)
        for i in FailedUrllist:
            print i
    else:
        print 'No link failed'
    
    print 'Mission Finished'

if __name__ == "__main__":

    #USNews
    #LiberalArts
    filename = 'Zinfo_'+'USNews'+'_List.txt'
    file_object = open(filename)
    List = file_object.readlines()
    file_object.close()
    
    for i in List[99:]:
        UniversityStart(i[:-1]+'programs/')
    






    
    
