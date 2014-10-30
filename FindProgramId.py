# -*- coding: UTF-8 -*-
import Config
import MySQLdb

def FindProgramId(UniversityName,Name,SchoolName,InstituteName):
    try:
        conn=MySQLdb.connect(host=Config.host,user=Config.user,passwd=Config.passwd,port=Config.port,db=Config.db,charset=Config.charset)
        cur=conn.cursor()
        cur.execute("SET NAMES utf8")

        FindUniversityIdStr="SELECT Id FROM university WHERE Name=%s"%UniversityName
        count=cur.execute(FindUniversityIdStr)
        if count == 0:
            AddUniversityStr = "INSERT INTO university(Name)VALUES(%s)"%UniversityName
            cur.execute(AddUniversityStr)
            cur.execute(FindUniversityIdStr)
        elif count == 1:
            pass
        else:
            print 'error in finding universityId'
            return None

        result = cur.fetchone()
        if result:
            UniversityId = str(result[0])
            print 'UniversityId:'+UniversityId
        else:
            print 'error in finding universityId'
            return None



        if not SchoolName == 'Null':
            FindSchoolIdStr = "SELECT Id FROM school WHERE Name=%s"%SchoolName
            count=cur.execute(FindSchoolIdStr)
            if count == 0:
                AddSchoolStr = "INSERT INTO school(UniversityId,Name)VALUES(%s,%s)"%(UniversityId,SchoolName)
                cur.execute(AddSchoolStr)
                cur.execute(FindSchoolIdStr)
            elif count == 1:
                pass
            else:
                print 'error in finding SchoolId'
                return None

            result = cur.fetchone()
            if result:
                SchoolId = str(result[0])
                print 'SchoolId:'+SchoolId
            else:
                print 'error in finding SchoolId'
                return None
        else:
            SchoolId = 'Null'
            print 'SchoolId:'+SchoolId



        FindProgramIdStr = "SELECT Id FROM program WHERE Name = %s AND UniversityId = %s"%(Name,UniversityId)
        count=cur.execute(FindProgramIdStr)
        if count == 0:
            AddProgramStr = "INSERT INTO program(UniversityId,Name,SchoolId,InstituteName)VALUES(%s,%s,%s,%s)"%(UniversityId,Name,SchoolId,InstituteName)
            cur.execute(AddProgramStr)
            cur.execute(FindProgramIdStr)
        elif count == 1:
            pass
        else:
            print 'error in finding ProgramId'
            return None

        result = cur.fetchone()
        if result:
            ProgramId = str(result[0])
            print 'ProgramId:'+ProgramId
        else:
            print 'error in finding ProgramId'
            return None

        conn.commit()
        cur.close()
        conn.close()
        return ProgramId

    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
         return None

if __name__ == "__main__":

    UniversityName = "'Carnegie Mellon University'"
    Name = "'Master of Software Engineering'"
    SchoolName = "'School of Computer Science'"
    InstituteName = "'Institute for Software Research'"

    print FindProgramId(UniversityName,Name,SchoolName,InstituteName)
