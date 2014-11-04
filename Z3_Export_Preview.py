import MySQLdb
import Config
import json

Listall = []

conn=MySQLdb.connect(host=Config.host,user=Config.user,passwd=Config.passwd,port=Config.port,db=Config.db,charset=Config.charset)
cur=conn.cursor()
str1 = "SELECT a.Id,b.Name,c.Name,a.DeadlineDate,b.DegreeType,a.Year,a.Season,b.Field,c.IconUrl,c.PicUrl,a.Timestamp from programinstance AS a,program AS b,university AS c WHERE A.ProgramId=b.Id AND b.UniversityId=c.Id "
cur.execute(str1)
result = cur.fetchall()
for i in result:

    dic = {
        'programInstanceId':i[0],
        'programName':i[1],
        'universityName':i[2],
        'DeadlineDate':str(i[3]),
        'DegreeType':i[4],
        'Year':i[5],
        'Season':i[6],
        'Field':i[7],
        'IconUrl':i[8],
        'PicUrl':i[9],
        'Timestamp':str(i[10]),
    }
    Listall.append(dic)
jsonStr = json.dumps(Listall);

file_object = open('ProgramInstancePreview.json', 'w')
file_object.write(jsonStr)
file_object.close()

cur.close()
conn.close()
