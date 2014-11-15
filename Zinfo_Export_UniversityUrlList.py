import Config

import urllib2
def url2str(url):
    request = urllib2.Request(url)  
    request.add_header('Cookie','sessionid=%s;'%Config.sessionid)  
    response = urllib2.urlopen(request).read()
    return response

import bs4
def start(url,filename):
    htmlstr = url2str(url)
    soup = bs4.BeautifulSoup(htmlstr)
    html = soup.html

    listall2=[]
    listall = html.findAll(lambda tag:tag.name=='a' and tag.parent.name=='div' and tag.parent.attrs.has_key('style'))
    for i in listall:
        str1 = 'https://www.applysquare.com'+i.attrs['href']+'\n'
        listall2.append(str1)
    
    file_object = open(filename, 'a')
    file_object.writelines(listall2)
    file_object.close()

def USNews():
    filename = 'Zinfo_'+'USNews'+'_List.txt'
    file_object = open(filename, 'w')
    file_object.write('')
    file_object.close()
    UrlList = []
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews&page=1')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews&page=2')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews&page=3')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews&page=4')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews&page=5')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews&page=6')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews&page=7')
    x=0
    for i in UrlList:
        x=x+1
        print '******  USNews  No.%d   ******'%x
        start(i,filename)

def LiberalArts():
    filename = 'Zinfo_'+'LiberalArts'+'_List.txt'
    file_object = open(filename, 'w')
    file_object.write('')
    file_object.close()
    UrlList = []
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_liberal_arts_college&page=1')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_liberal_arts_college&page=2')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_liberal_arts_college&page=3')
    x=0
    for i in UrlList:
        x=x+1
        print '******  LiberalArts  No.%d   ******'%x
        start(i,filename)

def QS():
    filename = 'Zinfo_'+'QS'+'_List.txt'
    file_object = open(filename, 'w')
    file_object.write('')
    file_object.close()
    UrlList = []
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:qs&page=1')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:qs&page=2')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:qs&page=3')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:qs&page=4')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:qs&page=5')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:qs&page=6')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:qs&page=7')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:qs&page=8')

    x=0
    for i in UrlList:
        x=x+1
        print '******  QS  No.%d   ******'%x
        start(i,filename)

def TIMES():
    filename = 'Zinfo_'+'TIMES'+'_List.txt'
    file_object = open(filename, 'w')
    file_object.write('')
    file_object.close()
    UrlList = []
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:times&page=1')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:times&page=2')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:times&page=3')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:times&page=4')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:times&page=5')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:times&page=6')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:times&page=7')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:times&page=8')

    x=0
    for i in UrlList:
        x=x+1
        print '******  TIMES  No.%d   ******'%x
        start(i,filename)

def usnews_school_engineering():
    name = 'usnews_school_engineering'
    filename = 'Zinfo_'+name+'_List.txt'
    file_object = open(filename, 'w')
    file_object.write('')
    file_object.close()
    UrlList = []
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_engineering&page=1')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_engineering&page=2')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_engineering&page=3')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_engineering&page=4')
    x=0
    for i in UrlList:
        x=x+1
        print '******  %s  No.%d   ******'%(name,x)
        start(i,filename)

def usnews_school_law():
    name = 'usnews_school_law'
    filename = 'Zinfo_'+name+'_List.txt'
    file_object = open(filename, 'w')
    file_object.write('')
    file_object.close()
    UrlList = []
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_law&page=1')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_law&page=2')
    x=0
    for i in UrlList:
        x=x+1
        print '******  %s  No.%d   ******'%(name,x)
        start(i,filename)

def usnews_school_business():
    name = 'usnews_school_business'
    filename = 'Zinfo_'+name+'_List.txt'
    file_object = open(filename, 'w')
    file_object.write('')
    file_object.close()
    UrlList = []
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_business&page=1')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_business&page=2')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_business&page=3')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_business&page=4')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_business&page=5')
    x=0
    for i in UrlList:
        x=x+1
        print '******  %s  No.%d   ******'%(name,x)
        start(i,filename)

def usnews_school_medical_primary_care():
    name = 'usnews_school_medical_primary_care'
    filename = 'Zinfo_'+name+'_List.txt'
    file_object = open(filename, 'w')
    file_object.write('')
    file_object.close()
    UrlList = []
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_medical_primary_care&page=1')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_medical_primary_care&page=2')
    x=0
    for i in UrlList:
        x=x+1
        print '******  %s  No.%d   ******'%(name,x)
        start(i,filename)

def usnews_school_medical_research():
    name = 'usnews_school_medical_research'
    filename = 'Zinfo_'+name+'_List.txt'
    file_object = open(filename, 'w')
    file_object.write('')
    file_object.close()
    UrlList = []
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_medical_research&page=1')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_medical_research&page=2')
    x=0
    for i in UrlList:
        x=x+1
        print '******  %s  No.%d   ******'%(name,x)
        start(i,filename)


def usnews_school_fine_arts():
    name = 'usnews_school_fine_arts'
    filename = 'Zinfo_'+name+'_List.txt'
    file_object = open(filename, 'w')
    file_object.write('')
    file_object.close()
    UrlList = []
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_fine_arts&page=1')
    UrlList.append('https://www.applysquare.com/zh-cn/search/?q=ranking:usnews_school_fine_arts&page=2')
    x=0
    for i in UrlList:
        x=x+1
        print '******  %s  No.%d   ******'%(name,x)
        start(i,filename)
        
if __name__ == "__main__":
    #USNews()
    #LiberalArts()
    #QS()
    #TIMES()
    #usnews_school_engineering()
    #usnews_school_law()
    #usnews_school_business()
    #usnews_school_medical_primary_care()
    #usnews_school_medical_research()
    usnews_school_fine_arts()


