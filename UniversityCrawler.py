# -*- coding: UTF-8 -*-
from Crawler import url2str,start
import bs4
def LinkList(UniversityUrl):
    htmlstr = url2str(UniversityUrl)
    soup = bs4.BeautifulSoup(htmlstr)
    html = soup.html
    MasterProject = html.find(lambda tag:tag.name=='h2' and tag.text.find(u'本科项目')>=0)
    listall = MasterProject.findAllNext(lambda tag:tag.name=='a' and tag.attrs.has_key('class') and tag.attrs['class'][0]=='clickable')
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

    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/princeton/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/harvard/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/yale/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/columbia/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/stanford/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/uchicago/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/duke/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/mit/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/upenn/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/caltech/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/dartmouth/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/jhu/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/northwestern/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/brown/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/wustl/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/cornell/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/vanderbilt/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/nd/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/rice/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/berkeley/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/emory/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/georgetown/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/cmu/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/ucla/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/usc/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/virginia/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/wfu/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/tufts/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/umich/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/unc/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/bc/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/brandeis/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/nyu/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/rochester/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/wm/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/gatech/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/case/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/psu/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/ucdavis/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/ucsd/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/bu/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/illinois/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/lehigh/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/rpi/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/ucsb/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/wisc/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/miami/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/yu/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/northeastern/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/uci/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/ufl/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/gwu/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/osu/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/tulane/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/utexas/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/washington/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/fordham/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/pepperdine/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/uconn/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/smu/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/uga/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/byu/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/clemson/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/pitt/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/syr/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/umd/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/wpi/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/purdue/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/rutgers/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/tamu/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/umn/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/vt/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/msu/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/uiowa/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/american/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/baylor/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/clarku/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/iub/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/marquette/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/muohio/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/udel/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/stevens/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/stonybrook/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/tcu/'#无项目
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/uvm/'#无项目
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/colorado/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/esf/'#无项目
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/uah/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/ucsc/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/utulsa/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/auburn/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/fsu/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/mines/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/sandiego/'#无项目
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/ucdenver/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/umass/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/binghamton/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/drexel/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/missouri/'
    UniversityUrl = 'https://www.applysquare.com/zh-cn/institute/unh/'
    
    UniversityStart(UniversityUrl)    




    






    
    
