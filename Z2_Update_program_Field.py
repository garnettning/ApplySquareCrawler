import MySQLdb
import Config

def SetField(FieldNum,ConditionStr):
    str1 = "UPDATE program SET Field = %d WHERE Field IS NULL AND "%FieldNum
    temp = str1+ConditionStr
    return temp

def SetSecondaryField(FieldNum,ConditionStr):
    str1 = "UPDATE program SET SecondaryField = %d WHERE Field != %d AND SecondaryField IS NULL AND "%(FieldNum,FieldNum)
    temp = str1+ConditionStr
    return temp

def UpdateDoubleField(FieldNum,ConditionStr):
    count=cur.execute(SetField(FieldNum,ConditionStr))
    print count
    count=cur.execute(SetSecondaryField(FieldNum,ConditionStr))
    print count

conn=MySQLdb.connect(host=Config.host,user=Config.user,passwd=Config.passwd,port=Config.port,db=Config.db,charset=Config.charset)
cur=conn.cursor()

#Clean programField
print 'Clean programField'
str1 = '''
UPDATE program SET Field = NULL,SecondaryField = NULL
'''
count=cur.execute(str1)
print count

#Aerospace / Aeronautical / Astronautical 101
print 'Aerospace / Aeronautical / Astronautical 101'
FieldNum = 101
ConditionStr = '''(
Name LIKE '%Aeros%'
OR Name LIKE '%Aeron%'
OR Name LIKE '%Astron%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Biological / Agricultural Engineering 102
print 'Biological / Agricultural Engineering 102'
FieldNum = 102
ConditionStr = '''(
Name LIKE '%Engineering%' AND
(
Name LIKE '%Agricul%'
OR Name LIKE '%Biological%'
)
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Biomedical / Bioengineering 103
print 'Biomedical / Bioengineering 103'
FieldNum = 103
ConditionStr = '''(
Name LIKE '%Biomedical%'
OR Name LIKE '%Bioengineering%'
OR Name LIKE '%Molecular%'
OR Name LIKE '%Cellular%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Chemical Engineering 104
print 'Chemical Engineering 104'
FieldNum = 104
ConditionStr = '''(
Name LIKE '%Engineering%' AND
(
Name LIKE '%Chemical%'
)
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Civil Engineering 105
print 'Civil Engineering 105'
FieldNum = 105
ConditionStr = '''(
Name LIKE '%Engineering%' AND
(
Name LIKE '%Civil%'
)
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Computer Engineering 106
print 'Computer Engineering 106'
FieldNum = 106
ConditionStr = '''(
Name LIKE '%Engineering%' AND
(
Name LIKE '%Computer%'
)
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Electrical / Electronic / Communications 107
print 'Electrical / Electronic / Communications 107'
FieldNum = 107
ConditionStr = '''(
Name LIKE '%Electrical%'
OR Name LIKE '%Electronic%'
OR Name LIKE '%Communication%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Environmental Engineering 108
print 'Environmental Engineering 108'
FieldNum = 108
ConditionStr = '''(
Name LIKE '%Engineering%' AND
(
Name LIKE '%Environment%'
)
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Industrial Engineering 109
print 'Industrial Engineering 109'
FieldNum = 109
ConditionStr = '''(
Name LIKE '%Industrial%'
OR Name LIKE '%Automotive%'
OR Name LIKE '%Manufacturing%'

)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Materials 110
print 'Materials 110'
FieldNum = 110
ConditionStr = '''(
Name LIKE '%Material%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Mechanical Engineering 111
print 'Mechanical Engineering 111'
FieldNum = 111
ConditionStr = '''(
Name LIKE '%Mechan%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Nuclear Engineering 112
print 'Nuclear Engineering 112'
FieldNum = 112
ConditionStr = '''(
Name LIKE '%Nuclear%'
OR Name LIKE '%Plasma%'
OR Name LIKE '%Radiological%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Statistics 201
print 'Statistics 201'
FieldNum = 201
ConditionStr = '''(
Name LIKE '%Statistic%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Biological Sciences 202
print 'Biological Sciences 202'
FieldNum = 202
ConditionStr = '''(
Name LIKE '%Bio%'
OR Name LIKE '%Neuroscience%'
OR Name LIKE '%Molecu%'
OR Name LIKE '%Cell%'
OR Name LIKE '%Organism%'
OR Name LIKE '%Genetics%'
OR Name LIKE '%Immunology%'
OR Name LIKE '%Ecology%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Chemistry 203
print 'Chemistry 203'
FieldNum = 203
ConditionStr = '''(
Name LIKE '%Chemistry%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Computer Science 204
print 'Computer Science 204'
FieldNum = 204
ConditionStr = '''(
(Name LIKE '%Comput%' AND Name LIKE '%Science%')
OR Name LIKE '%Robot%'
OR Name LIKE '%Algorithms%'
OR Name LIKE '%Combinatoric%'
OR Name LIKE '%Optimization%'
OR Name LIKE '%Software%'
OR Name LIKE '%Embedded%'
OR Name LIKE '%Graphics%'
OR Name LIKE '%Machine Learning%'
OR Name LIKE '%Data Science%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Earth Sciences 205
print 'Earth Sciences 205'
FieldNum = 205
ConditionStr = '''(
Name LIKE '%Earth%'
OR Name LIKE '%Geo%'
OR Name LIKE '%Planet%'
OR Name LIKE '%Meteorology%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Mathematics 206
print 'Mathematics 206'
FieldNum = 206
ConditionStr = '''(
Name LIKE '%Math%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Physics 207
print 'Physics 207'
FieldNum = 207
ConditionStr = '''(
Name LIKE '%Physics%'
OR Name LIKE '%Astronomy%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Actuarial Sciences 208
print 'Actuarial Sciences 208'
FieldNum = 208
ConditionStr = '''(
Name LIKE '%Actuar%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Philosophy 209
print 'Philosophy 209'
FieldNum = 209
ConditionStr = '''(
Name LIKE '%Philosophy%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Accounting 301
print 'Accounting 301'
FieldNum = 301
ConditionStr = '''(
Name LIKE '%Account%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Entrepreneurship 302
print 'Entrepreneurship 302'
FieldNum = 302
ConditionStr = '''(
Name LIKE '%Entrep%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Finance 304
print 'Finance 304'
FieldNum = 304
ConditionStr = '''(
Name LIKE '%Finance%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Financial Engineering 314
print 'Financial Engineering 314'
FieldNum = 314
ConditionStr = '''(
Name LIKE '%Engineering%' AND
(
Name LIKE '%Financial%'
)
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Information Systems 305
print 'Information Systems 305'
FieldNum = 305
ConditionStr = '''(
Name LIKE '%Information%'
OR Name LIKE '%Library%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#International Business 306
print 'International Business 306'
FieldNum = 306
ConditionStr = '''(
Name LIKE '%International%' AND Name LIKE '%Business%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Management 307
print 'Management 307'
FieldNum = 307
ConditionStr = '''(
Name LIKE '%Management%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Marketing 308
print 'Marketing 308'
FieldNum = 308
ConditionStr = '''(
Name LIKE '%Marketing%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Production / Operations 311
print 'Production / Operations 311'
FieldNum = 311
ConditionStr = '''(
Name LIKE '%Operation%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Supply Chain / Logistics 312
print 'Supply Chain / Logistics 312'
FieldNum = 312
ConditionStr = '''(
Name LIKE '%Chain%'
OR Name LIKE '%Logistics%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#MBA 313
print 'MBA 313'
FieldNum = 313
ConditionStr = '''(
Name LIKE '%MBA%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Human Resource Management 315
print 'Human Resource Management 315'
FieldNum = 315
ConditionStr = '''(
Name LIKE '%Human Resource%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Economics 402
print 'Economics 402'
FieldNum = 402
ConditionStr = '''(
Name LIKE '%Economic%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#English 403
print 'English 403'
FieldNum = 403
ConditionStr = '''(
Name LIKE '%English%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#History 404
print 'History 404'
FieldNum = 404
ConditionStr = '''(
Name LIKE '%History%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Psychology 405
print 'Psychology 405'
FieldNum = 405
ConditionStr = '''(
Name LIKE '%Psychology%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Political Science 406
print 'Political Science 406'
FieldNum = 406
ConditionStr = '''(
Name LIKE '%Politic%'
OR Name LIKE '%Policy%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Sociology 407
print 'Sociology 407'
FieldNum = 407
ConditionStr = '''(
Name LIKE '%Soci%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Public Affairs 408
print 'Public Affairs 408'
FieldNum = 408
ConditionStr = '''(
Name LIKE '%Affairs%'
OR Name LIKE '%MPA%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Anthropology 409
print 'Anthropology 409'
FieldNum = 409
ConditionStr = '''(
Name LIKE '%Anthropology%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Journalism and Mass Communication 410
print 'Journalism and Mass Communication 410'
FieldNum = 410
ConditionStr = '''(
Name LIKE '%Journalism%'
OR Name LIKE '%Mass%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Education 411
print 'Education 411'
FieldNum = 411
ConditionStr = '''(
Name LIKE '%Education%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Religion 412
print 'Religion 412'
FieldNum = 412
ConditionStr = '''(
Name LIKE '%Religion%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Linguistics 413
print 'Linguistics 413'
FieldNum = 413
ConditionStr = '''(
Name LIKE '%Linguistic%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Fine Arts 5
print 'Fine Arts 5'
FieldNum = 5
ConditionStr = '''(
Name LIKE '%Ceramics%'
OR Name LIKE '%Graphic Design%'
OR Name LIKE '%Industrial Design%'
OR Name LIKE '%Interior Design%'
OR Name LIKE '%Multimedia%'
OR Name LIKE '%Painting%'
OR Name LIKE '%Drawing%'
OR Name LIKE '%Photography%'
OR Name LIKE '%Printmaking%'
OR Name LIKE '%Sculpture%'
OR Name LIKE '%Literature%'
OR Name LIKE '%Architecture%'
OR Name LIKE '%Design%'
OR Name LIKE '%Art%'
OR Name LIKE '%MFA%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Public Health 8
print 'Public Health 8'
FieldNum = 8
ConditionStr = '''(
Name LIKE '%Health%'
OR Name LIKE '%Epidemiology%'
OR Name LIKE '%Nutrition%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Law 9
print 'Law 9'
FieldNum = 9
ConditionStr = '''(
Name LIKE '%Law%'
OR Name LIKE '%Legal%'
OR Name LIKE '%JD%'
OR Name LIKE '%JSD%'
OR Name LIKE '%LLM%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Medicine/Medical Science 10
print 'Medical 10'
FieldNum = 10
ConditionStr = '''(
Name LIKE '%Medicine%'
OR Name LIKE '%Pharmacology%'
OR Name LIKE '%Toxicology%'
OR Name LIKE '%Medical%'
OR Name LIKE '%Immunology%'
OR Name LIKE '%Pathology%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)




conn.commit()
cur.close()
conn.close()
import sys
sys.exit()

