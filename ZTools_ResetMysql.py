import Config
import MySQLdb
conn=MySQLdb.connect(host=Config.host,user=Config.user,passwd=Config.passwd,port=Config.port,db=Config.db,charset=Config.charset)
cur=conn.cursor()
cur.execute("SET NAMES utf8")

str1 = "TRUNCATE TABLE  `university`"
cur.execute(str1)

str1 = "ALTER TABLE  `university` AUTO_INCREMENT =1"
cur.execute(str1)

str1 = "TRUNCATE TABLE  `school`"
cur.execute(str1)

str1 = "ALTER TABLE  `school` AUTO_INCREMENT =1"
cur.execute(str1)

str1 = "TRUNCATE TABLE  `programinstance`"
cur.execute(str1)

str1 = "ALTER TABLE  `programinstance` AUTO_INCREMENT =1"
cur.execute(str1)

str1 = "TRUNCATE TABLE  `program`"
cur.execute(str1)

str1 = "ALTER TABLE  `program` AUTO_INCREMENT =1"
cur.execute(str1)

conn.commit()
cur.close()
conn.close()
print 'Rebuild OK!'
