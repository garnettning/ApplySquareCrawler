# -*- coding: utf-8 -*-
from Crawler import url2str

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

    PicUrl=html.find(lambda tag:tag.name=='img' and tag.attrs.has_key('class') and tag.attrs['class'][0]=='collapsed').attrs['src']
    print PicUrl
    
    Nickname = url[url.find(u'institute/')+10:-2]
    print Nickname

    UniversityName = html.find('h1',{'class':'ellipsis'}).contents[1].text.strip()
    print UniversityName

    Description = None
    ChineseName = None
    flag = html.find('div',{'class':'box-content'})
    if flag:
        temp = flag.find('div',{'class':'js-autocollapse-content'})
        if not temp:
            temp = flag
        Description = temp.text.strip()
        print Description
        
        temp = Description[:Description.find(u'（')].strip()
        if len(temp)>15:
            temp = Description[:Description.find(u'(')].strip()
            if len(temp)>15:
                temp = Description[:Description.find(u'，')].strip()
                if len(temp)>15:
                    temp = Description[:Description.find(u',')].strip()
                    if len(temp)>15:
                        temp = None
        ChineseName = temp
        print ChineseName

    
    import Config
    conn=MySQLdb.connect(host=Config.host,user=Config.user,passwd=Config.passwd,port=Config.port,db=Config.db,charset=Config.charset)
    cur=conn.cursor()

    FindUniversityIdStr="SELECT Id FROM university WHERE Name=%s"%c(UniversityName)
    count=cur.execute(FindUniversityIdStr)
    if count == 1:
        result = cur.fetchone()
        UniversityId = str(result[0])
        print UniversityId
        UpdateUniversitystr = "UPDATE university SET IconUrl = %s ,PicUrl = %s ,Nickname = %s ,ApplysquareUrl = %s ,Description = %s ,ChineseName = %s WHERE Id = %s LIMIT 1"%(c(IconUrl),c(PicUrl),c(Nickname),c(url),c(Description),c(ChineseName),c(UniversityId))
        cur.execute(UpdateUniversitystr)
        print 'Update OK'
        conn.commit()
        cur.close()
        conn.close()
        return True
    elif count == 0:
        AddUniversityStr = "INSERT INTO university(Name,IconUrl,PicUrl,Nickname,ApplysquareUrl,Description,ChineseName)VALUES(%s,%s,%s,%s,%s,%s,%s)"%(c(UniversityName),c(IconUrl),c(PicUrl),c(Nickname),c(url),c(Description),c(ChineseName))
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

    #USNews
    #LiberalArts
    
    filename = 'Zinfo_'+'LiberalArts'+'_List.txt'
    file_object = open(filename)
    List = file_object.readlines()
    file_object.close()
    
    x=0
    for i in List:
        x+=1
        print '\n******* No.%d ******'%x
        print 'Link = '+i
        UpdateMysqlUniversityInfo(i)
    
