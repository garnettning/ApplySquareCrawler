import urllib2
def url2str(url):
    request = urllib2.Request(url)  
    request.add_header('Cookie','sessionid=5okf24xbu774tecwn2f4p5u0mlkqubv6;')  
    response = urllib2.urlopen(request).read()
    return response

import MySQLdb
def c(item):
    if item == None:
        return 'Null'
    elif item == True:
        return '1'
    elif item == False:
        return '0'
    else:
        return "'"+MySQLdb.escape_string(item.encode("utf-8")).decode("utf-8")+"'"

import bs4
def UpdateMysqlUniversityInfo(url):
    htmlstr = url2str(url)
    soup = bs4.BeautifulSoup(htmlstr)
    html = soup.html

    IconUrl=html.find(lambda tag:tag.name=='img' and tag.attrs.has_key('height')).attrs['src']
    print IconUrl

    Nickname = url[url.find(u'institute/')+10:-1]
    print Nickname

    UniversityName = html.find('h1',{'class':'ellipsis'}).contents[1].text.strip()
    print UniversityName

    import Config
    conn=MySQLdb.connect(host=Config.host,user=Config.user,passwd=Config.passwd,port=Config.port,db=Config.db,charset=Config.charset)
    cur=conn.cursor()
    cur.execute("SET NAMES utf8")

    FindUniversityIdStr="SELECT Id FROM university WHERE Name=%s"%c(UniversityName)
    count=cur.execute(FindUniversityIdStr)
    if count == 1:
        result = cur.fetchone()
        UniversityId = str(result[0])
        print UniversityId
        UpdateUniversitystr = "UPDATE university SET IconUrl = %s ,Nickname = %s ,ApplysquareUrl = %s WHERE Id = %s LIMIT 1"%(c(IconUrl),c(Nickname),c(url),c(UniversityId))
        cur.execute(UpdateUniversitystr)
        print 'Update OK'
        conn.commit()
        cur.close()
        conn.close()
        return True
    elif count == 0:
        AddUniversityStr = "INSERT INTO university(Name,IconUrl,Nickname,ApplysquareUrl)VALUES(%s,%s,%s,%s)"%(c(UniversityName),c(IconUrl),c(Nickname),c(url))
        cur.execute(AddUniversityStr)
        print 'Creat OK'
        conn.commit()
        cur.close()
        conn.close()
        return True
    else:
        print 'error'
        conn.commit()
        cur.close()
        conn.close()
        return False
    

if __name__ == "__main__":
    
    from UrlList import List
    x=0
    for i in List:
        x+=1
        print '\n******* No.%d ******'%x
        print 'Link = '+i
        UpdateMysqlUniversityInfo(i)
    
