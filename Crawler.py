# -*- coding: UTF-8 -*-
import Config

import urllib2
def url2str(url):
    request = urllib2.Request(url)  
    request.add_header('Cookie','sessionid=%s;'%Config.sessionid)  
    response = urllib2.urlopen(request).read()
    return response

import bs4
import copy
def get_req_content(html,str1):
    box_req_title = html.find(lambda tag: tag.name=='div' and tag.attrs['class'][0]=='box-req-title' and tag.text.find(str1)>=0)
    if box_req_title:
        box_req_content = box_req_title.findNextSibling('div',{'class':'box-req-content'}).find('div',{'class':'js-autocollapse-content'})
        if not box_req_content:
            box_req_content = box_req_title.findNextSibling('div',{'class':'box-req-content'})
        return box_req_content
    else:
        return box_req_title

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

def start(url):
    try:
        htmlstr = url2str(url)
        soup = bs4.BeautifulSoup(htmlstr)
        html = soup.html

        #print '\n\n\n'
        #print '***************************************************************'
        #print '************************Program Table**************************'
        #print '***************************************************************'
        #UniversityName
        #print '\n'+'UniversityName: '
        UniversityName = html.find('h2',{'class':'ellipsis'}).contents[1].text.strip()
        #print UniversityName

        #ProgramName
        #print '\n'+'ProgramName: '
        ProgramName = html.find('h1',{'class':'ellipsis'}).contents[1].text.strip()
        #print ProgramName
        
        #SchoolName
        #print '\n'+'SchoolName: '
        if html.find('dt',text=u'学院'):
            SchoolName = html.find('dt',text=u'学院').findNextSibling('dd').text.strip()
            #print SchoolName
        else:
            SchoolName = None
            #print "N/A"

        #InstituteName
        #print '\n'+'InstituteName: '
        if html.find('dt',text=u'系'):
            InstituteName = html.find('dt',text=u'系').findNextSibling('dd').text.strip()
            #print InstituteName
        else:
            InstituteName = None
            #print "N/A"

        #print '\n\n\n'
        #print '***************************************************************'
        #print '***********************Program Instance************************'
        #print '***************************************************************'

        #Year
        #print '\n'+'Year: '
        if html.find('dt',text=u'学期'):
            str1 = soup.html.find('dt',text=u'学期').findNextSibling('dd').text.encode("utf-8")
            Year = filter(str.isdigit,str1)
            #print Year
        else:
            Year = None
            #print "N/A"
        
        #Season
        #print '\n'+'Season: '
        if html.find('dt',text=u'学期'):
            str1 = soup.html.find('dt',text=u'学期').findNextSibling('dd').text.encode("utf-8")
            Season = str1.strip()[5:]
            if Season=='春季':
                Season = '1'
            elif Season=='夏季':
                Season = '2'
            elif Season=='秋季':
                Season = '3'
            elif Season=='冬季':
                Season = '4'
            else:
                Season = '0'
            #print Season
        else:
            Season = None
            #print "N/A"

        #DegreeName
        #print '\n'+'DegreeName: '
        if html.find('dt',text=u'学位'):
            DegreeName = html.find('dt',text=u'学位').findNextSibling('dd').text.strip()
            #print DegreeName
        else:
            DegreeName = None
            #print "N/A"

        #DegreeLink
        #print '\n'+'DegreeLink: '
        if html.find('dt',text=u'学位'):
            DegreeLink = html.find('dt',text=u'链接').findNextSibling('dd').text.strip()
            #print DegreeLink
        else:
            DegreeLink = None
            #print "N/A"

         #ApplicationLink
        #print '\n'+'ApplicationLink: '
        if html.find('dt',text=u'网申登录链接'):
            ApplicationLink = html.find('dt',text=u'网申登录链接').findNextSibling('ul').li.a.text.strip()
            #print ApplicationLink
        else:
            ApplicationLink = None
            #print "N/A"

        #ContactName
        #print '\n'+'ContactName: '
        if html.find('ul',{'class':'list-unstyled'}):
            if html.find('ul',{'class':'list-unstyled'}).find(lambda tag: tag.name=='li' and len(tag)==1):
                ContactName = html.find('ul',{'class':'list-unstyled'}).find(lambda tag: tag.name=='li' and len(tag)==1).text.strip()
                #print ContactName
            else:
                ContactName = None
                #print "N/A"
        else:
            ContactName = None
            #print "N/A"

        #Email
        #print '\n'+'Email: '
        if html.find('i',{'class':'icon-envelope-alt icon-fixed-width'}):
            Email = html.find('i',{'class':'icon-envelope-alt icon-fixed-width'}).nextSibling.string.strip()
            #print Email
        else:
            Email = None
            #print "N/A"

        #PhoneNumber
        #print '\n'+'PhoneNumber: '
        if html.find('i',{'class':'icon-phone icon-fixed-width'}):
            PhoneNumber = html.find('i',{'class':'icon-phone icon-fixed-width'}).nextSibling.string.strip()
            #print PhoneNumber
        else:
            PhoneNumber = None
            #print "N/A"
            
        #print '\n\n\n'
        #print '***************************************************************'
        #print '**********************DeadLine Data****************************'
        #print '***************************************************************'
       
        #DeadlineStatus
        #print '\n'+'DeadlineStatus: '
        listall = html.find('div',{'class':'bg-title'}).findNextSibling('div',{'class':'box'}).div.dl.findAll('dd',{'class':None})
        DeadlineStatus = str(len(listall))
        #print DeadlineStatus

        #DeadlineDate
        #print '\n'+'DeadlineDate: '
        if DeadlineStatus == '1':
            DeadlineDate = listall[0].contents[1].text.strip()
            #print DeadlineDate
        else:
            DeadlineDate = None
            #print "N/A"

        #DeadlineString(JsonArray)
        #print '\n'+'DeadlineString(JsonArray): '
        if not DeadlineStatus == 0:
            Deadlinelist = []
            for item in listall:
                Name = item.contents[2].string.strip()
                Date = item.contents[1].text.strip()
                if item.findNextSibling('dd',{'class':'ellipsis'}):
                    Link = item.findNextSibling('dd',{'class':'ellipsis'}).a.text.strip()
                else:
                    Link = None
                dic = {'Name':Name,'Date':Date,'Link':Link}
                Deadlinelist+=[copy.deepcopy(dic)]
            import json
            DeadlineString = json.dumps(Deadlinelist);
            #print DeadlineString
        else:
            DeadlineString = None
            #print "N/A"

        #DeadlineOringin
        #print '\n'+'DeadlineOringin: '
        if html.find('div',{'class':'bg-title'}).findNextSibling('div',{'class':'box'}).div.find('dt',text=u'描述'):
            DeadlineOringin = html.find('div',{'class':'bg-title'}).findNextSibling('div',{'class':'box'}).div.find('dt',text=u'描述').findNextSibling('dd').text.strip()
            #print DeadlineOringin
        else:
            DeadlineOringin = None
            #print "N/A"

        #DeadlineLink
        #print '\n'+'DeadlineLink: '
        if html.find('div',{'class':'bg-title'}).findNextSibling('div',{'class':'box'}).div.find('dt',text=u'链接'):
            DeadlineLink = html.find('div',{'class':'bg-title'}).findNextSibling('div',{'class':'box'}).div.find('dt',text=u'链接').findNextSibling('dd').text.strip()
            #print DeadlineLink
        else:
            DeadlineLink = None
            #print "N/A"
        

      
        #print '\n\n\n'
        #print '***************************************************************'
        #print '******************Application Requirement**********************'
        #print '***************************************************************'

        #ApplicationFeeHas
        #print '\n'+'ApplicationFeeHas: '
        box_req_content = get_req_content(html,u'申请费')
        if box_req_content:
            ApplicationFeeHas = True
        else:
            ApplicationFeeHas = False
        #print ApplicationFeeHas
        
        #ApplicationFee
        #print '\n'+'ApplicationFee: '
        box_req_content = get_req_content(html,u'申请费')
        if box_req_content:
            tempstr = box_req_content.find(lambda tag: tag.name=='span' and tag.text.find(u'申请费')>=0)
            if tempstr:
                spanstr = tempstr.findNextSibling('span').text.strip()
                ApplicationFee = filter(str.isdigit,spanstr.encode("utf-8"))
            else:
                ApplicationFee = '0'
            #print ApplicationFee
        else:
            ApplicationFee = None
            #print "N/A"

        #ApplicationFeeType
        #print '\n'+'ApplicationFeeType: '
        box_req_content = get_req_content(html,u'申请费')
        if box_req_content:
            tempstr = box_req_content.find(lambda tag: tag.name=='span' and tag.text.find(u'申请费')>=0)
            if tempstr:
                spanstr = box_req_content.find(lambda tag: tag.name=='span' and tag.text.find(u'申请费')>=0).findNextSibling('span').text.strip()
                if spanstr.find(u'美元')>=0:
                    ApplicationFeeType = '1'
                    #print ApplicationFeeType
                else:  
                    ApplicationFeeType = None
                    #print "N/A"
            else:
                ApplicationFeeType = None
                #print "N/A"    
        else:
            ApplicationFeeType = None
            #print "N/A"

        #ApplicationFeeOrigin
        #print '\n'+'ApplicationFeeOrigin: '
        box_req_content = get_req_content(html,u'申请费')
        if box_req_content:
            flag = False
            for i in box_req_content.contents:
                if type(i)==bs4.element.NavigableString:
                    if len(i.string.strip())>1:
                        flag = True
                        ApplicationFeeOrigin = i.string.strip()
            if flag:
                ApplicationFeeOrigin = ApplicationFeeOrigin
                #print ApplicationFeeOrigin
            else:
                ApplicationFeeOrigin = None
                #print "N/A"
        else:
            ApplicationFeeOrigin = None
            #print "N/A"

        #print '\n'
        #print '******************ToeflIBT**********************'

        #ToeflHas
        #print '\n'+'ToeflHas: '
        box_req_content = get_req_content(html,u'托福')
        if box_req_content:
            ToeflHas = True
        else:
            ToeflHas = False
        #print ToeflHas
        
        #ToeflIBTTotal
        #print '\n'+'ToeflIBTTotal: '
        box_req_content = get_req_content(html,u'托福')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'总分')>=0)
            if Has_content:
                contentstr = Has_content.findNextSibling('span').text.strip()[0:10]
                ToeflIBTTotal = filter(str.isdigit,contentstr.encode("utf-8"))
                #print ToeflIBTTotal
            else:
                ToeflIBTTotal = None
                #print "N/A" 
        else:
            ToeflIBTTotal = None
            #print "N/A"

        #ToeflIBTReading
        #print '\n'+'ToeflIBTReading: '
        box_req_content = get_req_content(html,u'托福')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'阅读')>=0)
            if Has_content:
                contentstr = Has_content.findNextSibling('span').text.strip()[0:10]
                ToeflIBTReading = filter(str.isdigit,contentstr.encode("utf-8"))
                #print ToeflIBTReading
            else:
                ToeflIBTReading = None
                #print "N/A" 
        else:
            ToeflIBTReading = None
            #print "N/A"

        #ToeflIBTListening
        #print '\n'+'ToeflIBTListening: '
        box_req_content = get_req_content(html,u'托福')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'听力')>=0)
            if Has_content:
                contentstr = Has_content.findNextSibling('span').text.strip()[0:10]
                ToeflIBTListening = filter(str.isdigit,contentstr.encode("utf-8"))
                #print ToeflIBTListening
            else:
                ToeflIBTListening = None
                #print "N/A" 
        else:
            ToeflIBTListening = None
            #print "N/A"

        #ToeflIBTSpeaking
        #print '\n'+'ToeflIBTSpeaking: '
        box_req_content = get_req_content(html,u'托福')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'口语')>=0)
            if Has_content:
                contentstr = Has_content.findNextSibling('span').text.strip()[0:10]
                ToeflIBTSpeaking = filter(str.isdigit,contentstr.encode("utf-8"))
                #print ToeflIBTSpeaking
            else:
                ToeflIBTSpeaking = None
                #print "N/A" 
        else:
            ToeflIBTSpeaking = None
            #print "N/A"

        #ToeflIBTWriting
        #print '\n'+'ToeflIBTWriting: '
        box_req_content = get_req_content(html,u'托福')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'写作')>=0)
            if Has_content:
                contentstr = Has_content.findNextSibling('span').text.strip()[0:10]
                ToeflIBTWriting = filter(str.isdigit,contentstr.encode("utf-8"))
                #print ToeflIBTWriting
            else:
                ToeflIBTWriting = None
                #print "N/A" 
        else:
            ToeflIBTWriting = None
            #print "N/A"

        #ToeflIBTOrigin
        #print '\n'+'ToeflIBTOrigin: '
        box_req_content = get_req_content(html,u'托福')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='p' and len(tag)==1)
            if Has_content:
                ToeflIBTOrigin = Has_content.string.strip()
                #print ToeflIBTOrigin
            else:
                ToeflIBTOrigin = None
                #print "N/A" 
        else:
            ToeflIBTOrigin = None
            #print "N/A"

        #ToeflIBTNote
        #print '\n'+'ToeflIBTNote: '
        box_req_content = get_req_content(html,u'托福')
        if box_req_content:
            flag = False
            for i in box_req_content.contents:
                if type(i)==bs4.element.NavigableString:
                    if len(i.string.strip())>1:
                        flag = True
                        ToeflIBTNote = i.string.strip()
            if flag:
                ToeflIBTNote = ToeflIBTNote
                #print ToeflIBTNote
            else:
                ToeflIBTNote = None
                #print "N/A"
        else:
            ToeflIBTNote = None
            #print "N/A"

        #print '\n'
        #print '******************Ielts**********************'

        #IeltsHas
        #print '\n'+'IeltsHas: '
        box_req_content = get_req_content(html,u'雅思')
        if box_req_content:
            IeltsHas = True
        else:
            IeltsHas = False
        #print IeltsHas
        
        #IeltsTotal
        #print '\n'+'IeltsTotal: '
        box_req_content = get_req_content(html,u'雅思')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'总分')>=0)
            if Has_content:
                contentstr = Has_content.findNextSibling('span').text.strip()[0:10]
                IeltsTotal = filter(lambda x:str.isdigit(x) or x=='.',contentstr.encode("utf-8"))
                #print IeltsTotal
            else:
                IeltsTotal = None
                #print "N/A" 
        else:
            IeltsTotal = None
            #print "N/A"
        
        #IeltsReading
        #print '\n'+'IeltsReading: '
        box_req_content = get_req_content(html,u'雅思')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'阅读')>=0)
            if Has_content:
                contentstr = Has_content.findNextSibling('span').text.strip()[0:10]
                IeltsReading = filter(lambda x:str.isdigit(x) or x=='.',contentstr.encode("utf-8"))
                #print IeltsReading
            else:
                IeltsReading = None
                #print "N/A" 
        else:
            IeltsReading = None
            #print "N/A"

        #IeltsListening
        #print '\n'+'IeltsListening: '
        box_req_content = get_req_content(html,u'雅思')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'听力')>=0)
            if Has_content:
                contentstr = Has_content.findNextSibling('span').text.strip()[0:10]
                IeltsListening = filter(lambda x:str.isdigit(x) or x=='.',contentstr.encode("utf-8"))
                #print IeltsListening
            else:
                IeltsListening = None
                #print "N/A" 
        else:
            IeltsListening = None
            #print "N/A"

        #IeltsSpeaking
        #print '\n'+'IeltsSpeaking: '
        box_req_content = get_req_content(html,u'雅思')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'口语')>=0)
            if Has_content:
                contentstr = Has_content.findNextSibling('span').text.strip()[0:10]
                IeltsSpeaking = filter(lambda x:str.isdigit(x) or x=='.',contentstr.encode("utf-8"))
                #print IeltsSpeaking
            else:
                IeltsSpeaking = None
                #print "N/A" 
        else:
            IeltsSpeaking = None
            #print "N/A"

        #IeltsWriting
        #print '\n'+'IeltsWriting: '
        box_req_content = get_req_content(html,u'雅思')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'写作')>=0)
            if Has_content:
                contentstr = Has_content.findNextSibling('span').text.strip()[0:10]
                IeltsWriting = filter(lambda x:str.isdigit(x) or x=='.',contentstr.encode("utf-8"))
                #print IeltsWriting
            else:
                IeltsWriting = None
                #print "N/A" 
        else:
            IeltsWriting = None
            #print "N/A"

        #IeltsOrigin
        #print '\n'+'IeltsOrigin: '
        box_req_content = get_req_content(html,u'雅思')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='p' and len(tag)==1)
            if Has_content:
                IeltsOrigin = Has_content.string.strip()
                #print IeltsOrigin
            else:
                IeltsOrigin = None
                #print "N/A" 
        else:
            IeltsOrigin = None
            #print "N/A"

        #IeltsNote
        #print '\n'+'IeltsNote: '
        box_req_content = get_req_content(html,u'雅思')
        if box_req_content:
            flag = False
            for i in box_req_content.contents:
                if type(i)==bs4.element.NavigableString:
                    if len(i.string.strip())>1:
                        flag = True
                        IeltsNote = i.string.strip()
            if flag:
                IeltsNote = IeltsNote
                #print IeltsNote
            else:
                IeltsNote = None
                #print "N/A"
        else:
            IeltsNote = None
            #print "N/A"

        #print '\n'
        #print '******************GRE**********************'

        #GreHas
        #print '\n'+'GreHas: '
        box_req_content = get_req_content(html,u'GRE')
        if box_req_content:
            GreHas = True
        else:
            GreHas = False
        #print GreHas
        
        #GreTotal
        #print '\n'+'GreTotal: '
        box_req_content = get_req_content(html,u'GRE')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'总分')>=0)
            if Has_content:
                contentstr = Has_content.findNextSibling('span').text.strip()[0:10]
                GreTotal = filter(lambda x:str.isdigit(x) or x=='.',contentstr.encode("utf-8"))
                #print GreTotal
            else:
                GreTotal = None
                #print "N/A"
        else:
            GreTotal = None
            #print "N/A"
            
        #GreVerbal
        #print '\n'+'GreVerbal: '
        box_req_content = get_req_content(html,u'GRE')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'Verbal')>=0)
            if Has_content:
                contentstr = Has_content.findNextSibling('span').text.strip()[0:10]
                GreVerbal = filter(lambda x:str.isdigit(x) or x=='.',contentstr.encode("utf-8"))
                #print GreVerbal
            else:
                GreVerbal = None
                #print "N/A" 
        else:
            GreVerbal = None
            #print "N/A"

        #GreQuantitative
        #print '\n'+'GreQuantitative: '
        box_req_content = get_req_content(html,u'GRE')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'Quantitative')>=0)
            if Has_content:
                contentstr = Has_content.findNextSibling('span').text.strip()[0:10]
                GreQuantitative = filter(lambda x:str.isdigit(x) or x=='.',contentstr.encode("utf-8"))
                #print GreQuantitative
            else:
                GreQuantitative = None
                #print "N/A" 
        else:
            GreQuantitative = None
            #print "N/A"

        #GreWriting
        #print '\n'+'GreWriting: '
        box_req_content = get_req_content(html,u'GRE')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'Writing')>=0)
            if Has_content:
                contentstr = Has_content.findNextSibling('span').text.strip()[0:10]
                GreWriting = filter(lambda x:str.isdigit(x) or x=='.',contentstr.encode("utf-8"))
                #print GreWriting
            else:
                GreWriting = None
                #print "N/A" 
        else:
            GreWriting = None
            #print "N/A"

        #GreOrigin
        #print '\n'+'GreOrigin: '
        box_req_content = get_req_content(html,u'GRE')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='p' and len(tag)==1 and len(tag.text)>50)
            if Has_content:
                GreOrigin = Has_content.string.strip()
                #print GreOrigin
            else:
                GreOrigin = None
                #print "N/A" 
        else:
            GreOrigin = None
            #print "N/A"

        #GreNote
        #print '\n'+'GreNote: '
        box_req_content = get_req_content(html,u'GRE')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='p' and len(tag)==1)
            if Has_content:
                GreNote = Has_content.string.strip()
                #print GreNote
            else:
                GreNote = None
                #print "N/A" 
        else:
            GreNote = None
            #print "N/A"
            
        #print '\n'
        #print '******************DegreeRequire**********************'
        
        #DegreeRequireHas
        #print '\n'+'DegreeRequireHas: '
        box_req_content = get_req_content(html,u'学历要求')
        if box_req_content:
            DegreeRequireHas = True
        else:
            DegreeRequireHas = False
        #print DegreeRequireHas
        
        #DegreeRequire
        #print '\n'+'DegreeRequire: '
        box_req_content = get_req_content(html,u'学历要求')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='dt' and tag.text.find(u'学历要求')>=0)
            if Has_content:
                DegreeRequire = Has_content.findNextSibling('dd').text.strip()
                #print DegreeRequire
            else:
                DegreeRequire = None
                #print "N/A" 
        else:
            DegreeRequire = None
            #print "N/A"

        #CourseRequire
        #print '\n'+'CourseRequire: '
        box_req_content = get_req_content(html,u'学历要求')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='dt' and tag.text.find(u'课程要求')>=0)
            if Has_content:
                CourseRequire = Has_content.findNextSibling('dd').text.strip()
                #print CourseRequire
            else:
                CourseRequire = None
                #print "N/A" 
        else:
            CourseRequire = None
            #print "N/A"
        
        #MajorRequire
        #print '\n'+'MajorRequire: '
        box_req_content = get_req_content(html,u'学历要求')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='dt' and tag.text.find(u'专业要求')>=0)
            if Has_content:
                MajorRequire = Has_content.findNextSibling('dd').text.strip()
                #print MajorRequire
            else:
                MajorRequire = None
                #print "N/A" 
        else:
            MajorRequire = None
            #print "N/A"

        #print '\n'
        #print '******************Transcript**********************'

        #TranscriptHas
        #print '\n'+'TranscriptHas: '
        box_req_content = get_req_content(html,u'成绩单')
        if box_req_content:
            TranscriptHas = True
        else:
            TranscriptHas = False
        #print TranscriptHas
        
        #TranscriptNote
        #print '\n'+'TranscriptNote: '
        box_req_content = get_req_content(html,u'成绩单')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'项目特别要求')>=0)
            if Has_content:
                TranscriptNote = Has_content.findNextSibling('p').text.strip()
                #print TranscriptNote
            else:
                TranscriptNote = None
                #print "N/A" 
        else:
            TranscriptNote = None
            #print "N/A"

        #TranscriptOringin
        #print '\n'+'TranscriptOringin: '
        box_req_content = get_req_content(html,u'成绩单')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'描述')>=0)
            if Has_content:
                TranscriptOringin = Has_content.findNextSibling('p').text.strip()
                #print TranscriptOringin
            else:
                TranscriptOringin = None
                #print "N/A" 
        else:
            TranscriptOringin = None
            #print "N/A"

        #print '\n'
        #print '******************PS**********************'

        #PsHas
        #print '\n'+'PsHas: '
        box_req_content = get_req_content(html,u'PS')
        if box_req_content:
            PsHas = True
        else:
            PsHas = False
        #print PsHas

        #PsOrigin
        #print '\n'+'PsOrigin: '
        box_req_content = get_req_content(html,u'PS')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'项目特别要求')>=0)
            if Has_content:
                PsOrigin = Has_content.findNextSibling('p').text.strip()
                #print PsOrigin
            else:
                PsOrigin = None
                #print "N/A" 
        else:
            PsOrigin = None
            #print "N/A"

        #PsNote
        #print '\n'+'PsNote: '
        box_req_content = get_req_content(html,u'PS')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='p' and len(tag)==1)
            if Has_content:
                PsNote = Has_content.string.strip()
                #print PsNote
            else:
                PsNote = None
                #print "N/A" 
        else:
            PsNote = None
            #print "N/A"

        #print '\n'
        #print '******************Resume**********************'

        #ResumeHas
        #print '\n'+'ResumeHas: '
        box_req_content = get_req_content(html,u'简历')
        if box_req_content:
            ResumeHas = True
        else:
            ResumeHas = False
        #print ResumeHas

        #ResumeOrigin
        #print '\n'+'ResumeOrigin: '
        box_req_content = get_req_content(html,u'简历')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'项目特别要求')>=0)
            if Has_content:
                ResumeOrigin = Has_content.findNextSibling('p').text.strip()
                #print ResumeOrigin
            else:
                ResumeOrigin = None
                #print "N/A" 
        else:
            ResumeOrigin = None
            #print "N/A"

        #ResumeNote
        #print '\n'+'ResumeNote: '
        box_req_content = get_req_content(html,u'简历')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='p' and len(tag)==1)
            if Has_content:
                ResumeNote = Has_content.string.strip()
                #print ResumeNote
            else:
                ResumeNote = None
                #print "N/A" 
        else:
            ResumeNote = None
            #print "N/A"

       
        #print '\n'
        #print '******************Recommendation**********************'

        #RecommendationHas
        #print '\n'+'RecommendationHas: '
        box_req_content = get_req_content(html,u'推荐信')
        if box_req_content:
            RecommendationHas = True
        else:
            RecommendationHas = False
        #print RecommendationHas

        #RecommendationNum
        #print '\n'+'RecommendationNum: '
        box_req_content = get_req_content(html,u'推荐信')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'数量')>=0)
            if Has_content:
                RecommendationNum = Has_content.findNextSibling('p').text.strip()
                #print RecommendationNum
            else:
                RecommendationNum = None
                #print "N/A" 
        else:
            RecommendationNum = None
            #print "N/A"

        #RecommendationOrigin
        #print '\n'+'RecommendationOrigin: '
        box_req_content = get_req_content(html,u'推荐信')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'项目特别要求')>=0)
            if Has_content:
                RecommendationOrigin = Has_content.findNextSibling('p').text.strip()
                #print RecommendationOrigin
            else:
                RecommendationOrigin = None
                #print "N/A" 
        else:
            RecommendationOrigin = None
            #print "N/A"



        #print '\n'
        #print '******************WorkExp**********************'

        #WorkExpHas
        #print '\n'+'WorkExpHas: '
        box_req_content = get_req_content(html,u'Work Experience')
        if box_req_content:
            WorkExpHas = True
        else:
            WorkExpHas = False
        #print WorkExpHas

        #WorkExpOrigin
        #print '\n'+'WorkExpOrigin: '
        box_req_content = get_req_content(html,u'Work Experience')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'项目特别要求')>=0)
            if Has_content:
                WorkExpOrigin = Has_content.findNextSibling('p').text.strip()
                #print WorkExpOrigin
            else:
                WorkExpOrigin = None
                #print "N/A" 
        else:
            WorkExpOrigin = None
            #print "N/A"

        #print '\n'
        #print '******************ProjectExp**********************'

        #ProjectExpHas
        #print '\n'+'ProjectExpHas: '
        box_req_content = get_req_content(html,u'project')
        if box_req_content:
            ProjectExpHas = True
        else:
            ProjectExpHas = False
        #print ProjectExpHas

        #ProjectExpOrigin
        #print '\n'+'ProjectExpOrigin: '
        box_req_content = get_req_content(html,u'project')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'项目特别要求')>=0)
            if Has_content:
                ProjectExpOrigin = Has_content.findNextSibling('p').text.strip()
                #print ProjectExpOrigin
            else:
                ProjectExpOrigin = None
                #print "N/A" 
        else:
            ProjectExpOrigin = None
            #print "N/A"

        #SATorACTHas
        #print '\n'+'SATorACTHas: '
        box_req_content = get_req_content(html,u'SAT and ACT')
        if box_req_content:
            SATorACTHas = True
        else:
            SATorACTHas = False
        #print SATorACTHas

        #SATorACTOrigin
        #print '\n'+'SATorACTOrigin: '
        box_req_content = get_req_content(html,u'SAT and ACT')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'项目特别要求')>=0)
            if Has_content:
                SATorACTOrigin = Has_content.findNextSibling('p').text.strip()
                #print SATorACTOrigin
            else:
                SATorACTOrigin = None
                #print "N/A" 
        else:
            SATorACTOrigin = None
            #print "N/A"
            
        
        #SATsubjecttestsHas
        #print '\n'+'SATsubjecttestsHas: '
        box_req_content = get_req_content(html,u'SAT subject tests')
        if box_req_content:
            SATsubjecttestsHas = True
        else:
            SATsubjecttestsHas = False
        #print SATsubjecttestsHas

        #SATsubjecttestsOrigin
        #print '\n'+'SATsubjecttestsOrigin: '
        box_req_content = get_req_content(html,u'SAT subject tests')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'项目特别要求')>=0)
            if Has_content:
                SATsubjecttestsOrigin = Has_content.findNextSibling('p').text.strip()
                #print SATsubjecttestsOrigin
            else:
                SATsubjecttestsOrigin = None
                #print "N/A" 
        else:
            SATsubjecttestsOrigin = None
            #print "N/A"

        #APExamsHas
        #print '\n'+'APExamsHas: '
        box_req_content = get_req_content(html,u'Advanced Placement (AP) exams')
        if box_req_content:
            APExamsHas = True
        else:
            APExamsHas = False
        #print APExamsHas

        #APExamsOrigin
        #print '\n'+'APExamsOrigin: '
        box_req_content = get_req_content(html,u'Advanced Placement (AP) exams')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'项目特别要求')>=0)
            if Has_content:
                APExamsOrigin = Has_content.findNextSibling('p').text.strip()
                #print APExamsOrigin
            else:
                APExamsOrigin = None
                #print "N/A" 
        else:
            APExamsOrigin = None
            #print "N/A"

        #WritingSampleHas
        #print '\n'+'WritingSampleHas: '
        box_req_content = get_req_content(html,u'Writing Sample')
        if box_req_content:
            WritingSampleHas = True
        else:
            WritingSampleHas = False
        #print WritingSampleHas

        #WritingSampleNote
        #print '\n'+'WritingSampleNote: '
        box_req_content = get_req_content(html,u'Writing Sample')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='p' and len(tag)==1)
            if Has_content:
                WritingSampleNote = Has_content.string.strip()
                #print WritingSampleNote
            else:
                WritingSampleNote = None
                #print "N/A" 
        else:
            WritingSampleNote = None
            #print "N/A"

        #TeacherEvaluationsHas
        #print '\n'+'TeacherEvaluationsHas: '
        box_req_content = get_req_content(html,u'Teacher Evaluations')
        if box_req_content:
            TeacherEvaluationsHas = True
        else:
            TeacherEvaluationsHas = False
        #print TeacherEvaluationsHas

        #TeacherEvaluationsNote
        #print '\n'+'TeacherEvaluationsNote: '
        box_req_content = get_req_content(html,u'Teacher Evaluations')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='p' and len(tag)==1)
            if Has_content:
                TeacherEvaluationsNote = Has_content.string.strip()
                #print TeacherEvaluationsNote
            else:
                TeacherEvaluationsNote = None
                #print "N/A" 
        else:
            TeacherEvaluationsNote = None
            #print "N/A"
        
        #SchoolReportHas
        #print '\n'+'SchoolReportHas: '
        box_req_content = get_req_content(html,u'学校报告')
        if box_req_content:
            SchoolReportHas = True
        else:
            SchoolReportHas = False
        #print SchoolReportHas

        #SchoolReportNote
        #print '\n'+'SchoolReportNote: '
        box_req_content = get_req_content(html,u'学校报告')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='p' and len(tag)==1)
            if Has_content:
                SchoolReportNote = Has_content.string.strip()
                #print SchoolReportNote
            else:
                SchoolReportNote = None
                #print "N/A" 
        else:
            SchoolReportNote = None
            #print "N/A"


        
        #ScoreChoiceHas
        #print '\n'+'ScoreChoiceHas: '
        box_req_content = get_req_content(html,u'Score Choice')
        if box_req_content:
            ScoreChoiceHas = True
        else:
            ScoreChoiceHas = False
        #print ScoreChoiceHas

        #ScoreChoiceOrigin
        #print '\n'+'ScoreChoiceOrigin: '
        box_req_content = get_req_content(html,u'Score Choice')
        if box_req_content:
            Has_content = box_req_content.find(lambda tag: tag.name=='strong' and tag.text.find(u'项目特别要求')>=0)
            if Has_content:
                ScoreChoiceOrigin = Has_content.findNextSibling('p').text.strip()
                #print ScoreChoiceOrigin
            else:
                ScoreChoiceOrigin = None
                #print "N/A" 
        else:
            ScoreChoiceOrigin = None
            #print "N/A"

        #InternationalStudentNoticeHas
        #print '\n'+'InternationalStudentNoticeHas: '
        box_req_content = get_req_content(html,u'国际学生注意事项')
        if box_req_content:
            InternationalStudentNoticeHas = True
        else:
            InternationalStudentNoticeHas = False
        #print InternationalStudentNoticeHas

        #InternationalStudentNoticeOrigin
        #print '\n'+'InternationalStudentNoticeOrigin: '
        box_req_content = get_req_content(html,u'国际学生注意事项')
        if box_req_content:
            flag = False
            for i in box_req_content.contents:
                if type(i)==bs4.element.NavigableString:
                    if len(i.string.strip())>1:
                        flag = True
                        InternationalStudentNoticeOrigin = i.string.strip()
            if flag:
                InternationalStudentNoticeOrigin = InternationalStudentNoticeOrigin
                #print InternationalStudentNoticeOrigin
            else:
                InternationalStudentNoticeOrigin = None
                #print "N/A"
        else:
            InternationalStudentNoticeOrigin = None
            #print "N/A"

        #print '\n\n\n'
        #print '***************************************************************'
        #print '**************************Others*******************************'
        #print '***************************************************************'

        #DataFrom
        #print '\n'+'DataFrom: '
        DataFrom = 'ApplySquare'
        #print DataFrom

        #DataLink
        #print '\n'+'DataLink: '
        DataLink = url
        #print DataLink
    except:
        print 'Error in Analysising Webpage'
        return False

    #print '\n\n\n'
    #print '###############################################################'
    #print '#########################   Mysql   ###########################'
    #print '###############################################################'

    import MySQLdb
    try:        
        #用UniversityName,ProgramName,SchoolName,InstituteName，经过一系列数据库处理，得到ProgramId
        from FindProgramId import FindProgramId
        ProgramId = FindProgramId(c(UniversityName),c(ProgramName),c(SchoolName),c(InstituteName))
        if ProgramId:
            conn=MySQLdb.connect(host=Config.host,user=Config.user,passwd=Config.passwd,port=Config.port,db=Config.db,charset=Config.charset)
            cur=conn.cursor()
            #检查有没有重复的programinstance
            #CheckStr = 'SELECT Id FROM programinstance WHERE Id = %s AND Year = %s AND Season = %s'%(c(ProgramId),c(Year),c(Season))
            CheckStr = 'SELECT Id FROM programinstance WHERE DataLink = %s'%c(DataLink)
            count=cur.execute(CheckStr)
            if count == 0: #没有的话就插入一条programinstance
                str2mysql = "INSERT INTO `haile`.`programinstance` VALUES (NULL, \
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, Null);"\
                %(c(ProgramId),c(Year),c(Season),c(DegreeName),c(DegreeLink),c(ApplicationLink),c(ContactName),c(Email),c(PhoneNumber),\
                c(DeadlineStatus),c(DeadlineDate),c(DeadlineString),c(DeadlineOringin),c(DeadlineLink),c(ApplicationFeeHas),c(ApplicationFee),c(ApplicationFeeType),c(ApplicationFeeOrigin),c(ToeflHas),\
                c(ToeflIBTTotal),c(ToeflIBTReading),c(ToeflIBTListening),c(ToeflIBTSpeaking),c(ToeflIBTWriting),c(ToeflIBTOrigin),c(ToeflIBTNote),c(IeltsHas),c(IeltsTotal),c(IeltsReading),\
                c(IeltsListening),c(IeltsSpeaking),c(IeltsWriting),c(IeltsOrigin),c(IeltsNote),c(GreHas),c(GreTotal),c(GreVerbal),c(GreQuantitative),c(GreWriting),\
                c(GreOrigin),c(GreNote),c(DegreeRequireHas),c(DegreeRequire),c(CourseRequire),c(MajorRequire),c(TranscriptHas),c(TranscriptNote),c(TranscriptOringin),c(PsHas),\
                c(PsOrigin),c(PsNote),c(ResumeHas),c(ResumeOrigin),c(ResumeNote),c(RecommendationHas),c(RecommendationNum),c(RecommendationOrigin),c(WorkExpHas),c(WorkExpOrigin),\
                c(ProjectExpHas),c(ProjectExpOrigin),c(SATorACTHas),c(SATorACTOrigin),c(SATsubjecttestsHas),c(SATsubjecttestsOrigin),c(APExamsHas),c(APExamsOrigin),c(WritingSampleHas),c(WritingSampleNote),\
                c(TeacherEvaluationsHas),c(TeacherEvaluationsNote),c(SchoolReportHas),c(SchoolReportNote),c(ScoreChoiceHas),c(ScoreChoiceOrigin),c(InternationalStudentNoticeHas),c(InternationalStudentNoticeOrigin),c(DataFrom),c(DataLink))
                cur.execute(str2mysql)
                conn.commit()
                cur.close()
                conn.close()
                print 'INSERT OK!'
                return True
            else:#有一条了，就不写入了
                cur.close()
                conn.close()
                print 'Already Had this programinstance!'
                return False        
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False
            
if __name__ == "__main__":
    url='https://www.applysquare.com/zh-cn/program/p5m2wa5a2s0m6zyv/'
    print start(url)
