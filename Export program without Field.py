import MySQLdb
import Config

conn=MySQLdb.connect(host=Config.host,user=Config.user,passwd=Config.passwd,port=Config.port,db=Config.db,charset=Config.charset)
cur=conn.cursor()

print 'Clean programField'
str1 = '''
SELECT Name
FROM program
WHERE Field IS NULL 
'''
count=cur.execute(str1)

result = cur.fetchall()

for i in result:
    print i[0]
