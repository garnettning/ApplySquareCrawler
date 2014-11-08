import MySQLdb
import Config

conn=MySQLdb.connect(host=Config.host,user=Config.user,passwd=Config.passwd,port=Config.port,db=Config.db,charset=Config.charset)
cur=conn.cursor()

#Clean programDegreeType
print 'Clean programDegreeType'
str1 = '''
UPDATE program SET DegreeType = NULL
'''
count=cur.execute(str1)
print count


#Bechelor
print 'Bechelor'
str1 = '''
UPDATE program,programinstance SET program.DegreeType = 1 WHERE 
program.Id=programinstance.ProgramId
AND program.DegreeType IS NULL
AND program.Name LIKE '%Undergraduate-Freshman%'
'''
count=cur.execute(str1)
print count


#Master
print 'Master'
str1 = '''
UPDATE program,programinstance SET program.DegreeType = 2 WHERE 
program.Id=programinstance.ProgramId AND
(
DegreeName LIKE  '%master%'
OR DegreeName LIKE  '%mba%'
OR DegreeName LIKE  '%ma%'
OR DegreeName LIKE  '%me%'
)
And NOT
(
   DegreeName LIKE  '%doctor%'
OR DegreeName LIKE  '%phd%'
)
'''
count=cur.execute(str1)
print count

#Doctor
print 'Doctor'
str1 = '''
UPDATE program,programinstance SET program.DegreeType = 3 WHERE 
program.Id=programinstance.ProgramId 
AND
(
   DegreeName LIKE  '%doctor%'
OR DegreeName LIKE  '%phd%'
)
And NOT
(
DegreeName LIKE  '%master%'
OR DegreeName LIKE  '%mba%'
OR DegreeName LIKE  '%ma%'
OR DegreeName LIKE  '%me%'
)
'''
count=cur.execute(str1)
print count

conn.commit()
cur.close()
conn.close()

