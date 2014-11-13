import Config

import urllib2
def url2str(url):
    request = urllib2.Request(url)  
    request.add_header('Cookie','sessionid=%s;'%Config.sessionid)  
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
