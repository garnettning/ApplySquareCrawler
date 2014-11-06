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


#####################################################
##############         Engineering 1     ############
#####################################################

#Aerospace / Aeronautical / Astronautical 101
print 'Aerospace / Aeronautical / Astronautical 101'
FieldNum = 101
ConditionStr = '''(
Name LIKE '%Aeros%'
OR Name LIKE '%Aeron%'
OR Name LIKE '%Astron%'
OR Name LIKE '%space%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Biological / Agricultural Engineering 102
print 'Biological / Agricultural Engineering 102'
FieldNum = 102
ConditionStr = '''(
(
Name LIKE '%Engineering%' AND
(
Name LIKE '%Agricul%'
OR Name LIKE '%Biological%'
)
)
OR Name LIKE '%agronom%'
OR Name LIKE '%Agricultural%'
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
OR Name LIKE '%petroleum%'
)
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Civil Engineering 105
print 'Civil Engineering 105'
FieldNum = 105
ConditionStr = '''(
(Name LIKE '%Engineering%' AND Name LIKE '%Civil%')
OR Name LIKE '%Structu%'
OR Name LIKE '%Transportation%'
OR Name LIKE '%Civil system%'
OR Name LIKE '%building%'
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
OR Name LIKE '%optical%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Environmental Engineering 108
print 'Environmental Engineering 108'
FieldNum = 108
ConditionStr = '''(
Name LIKE '%Environment%'
OR Name LIKE '%Energy%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Industrial Engineering 109
print 'Industrial Engineering 109'
FieldNum = 109
ConditionStr = '''(
Name LIKE '%Industrial%'
OR Name LIKE '%Automotive%'
OR Name LIKE '%Manufacturing%'
OR Name LIKE '%quality%'
OR (Name LIKE '%system%' AND Name LIKE '%Engineering%')
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Materials 110
print 'Materials 110'
FieldNum = 110
ConditionStr = '''(
Name LIKE '%Material%'
OR Name LIKE '%nano%'
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

#####################################################
##############          Science 2        ############
#####################################################

#Statistics 201
print 'Statistics 201'
FieldNum = 201
ConditionStr = '''(
Name LIKE '%Statistic%'
OR Name LIKE '%quantitative%'
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
OR Name LIKE '%entomology%'
OR Name LIKE '%Gene%'
OR Name LIKE '%Immunology%'
OR Name LIKE '%Ecology%'
OR Name LIKE '%plant%'
OR Name LIKE '%animal%'
OR Name LIKE '%wildlife%'
OR Name LIKE '%zoology%'
OR Name LIKE '%botany%'
OR Name LIKE '%horticultur%'
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
OR Name LIKE '%neural system%'
OR Name LIKE '%computational%'
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
OR Name LIKE '%Environmental%'
OR Name LIKE '%Forest%'
OR Name LIKE '%ocean%'
OR Name LIKE '%marine%'
OR Name LIKE '%atmosph%'
OR Name LIKE '%soil%'
OR Name LIKE '%Natur%'
OR Name LIKE '%sustainab%'
OR Name LIKE '%water%'
OR Name LIKE '%hydrology%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Mathematics 206
print 'Mathematics 206'
FieldNum = 206
ConditionStr = '''(
Name LIKE '%Math%'
OR Name LIKE '%computation%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Physics 207
print 'Physics 207'
FieldNum = 207
ConditionStr = '''(
Name LIKE '%Physic%'
OR Name LIKE '%Astronom%'
OR Name LIKE '%fluid%'
OR Name LIKE '%optics%'
OR Name LIKE '%photoni%'
OR Name LIKE '%acoustics%'
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


#####################################################
##############          Business 3       ############
#####################################################

#Accounting 301
print 'Accounting 301'
FieldNum = 301
ConditionStr = '''(
Name LIKE '%Account%'
OR Name LIKE '%Acct%'
OR Name LIKE '%tax%'
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
OR Name LIKE '%strategy%'
OR Name LIKE '%Organization%'
OR Name LIKE '%decision%'
OR Name LIKE '%Leadership%'
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
OR Name LIKE '%Business Administration%'
OR Name LIKE '%M.B.A%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Human Resource Management 315
print 'Human Resource Management 315'
FieldNum = 315
ConditionStr = '''(
Name LIKE '%Human Resource%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)


#####################################################
############        Social Sciences 4      ##########
#####################################################

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
OR Name LIKE '%TESOL%'
OR Name LIKE '%writing%'
OR Name LIKE '%rhetoric%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#History 404
print 'History 404'
FieldNum = 404
ConditionStr = '''(
Name LIKE '%Histor%'
OR Name LIKE '%archaeolog%'
OR Name LIKE '%egyptology%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Psychology 405
print 'Psychology 405'
FieldNum = 405
ConditionStr = '''(
Name LIKE '%Psycholog%'
OR Name LIKE '%brain%'
OR Name LIKE '%cognit%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Political Science 406
print 'Political Science 406'
FieldNum = 406
ConditionStr = '''(
Name LIKE '%Politic%'
OR Name LIKE '%Policy%'
OR Name LIKE '%Government%'
OR Name LIKE '%security%'
OR Name LIKE '%international relation%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Sociology 407
print 'Sociology 407'
FieldNum = 407
ConditionStr = '''(
Name LIKE '%Soci%'
OR Name LIKE '%Policy%'
OR Name LIKE '%Asia%'
OR Name LIKE '%East%'
OR Name LIKE '%Africa%'
OR Name LIKE '%russian%'
OR Name LIKE '%cultur%'
OR Name LIKE '%german%'
OR Name LIKE '%roman%'
OR Name LIKE '%family%'
OR Name LIKE '%Arab%'
OR Name LIKE '%medieval%'
OR Name LIKE '%Feminist%'
OR Name LIKE '%American Studies%'
OR Name LIKE '%hispanic%'
OR Name LIKE '%indian%'
OR Name LIKE '%population%'
OR Name LIKE '%demograph%'
OR Name LIKE '%jewish%'
OR Name LIKE '%civilization%'
OR Name LIKE '%Humanit%'
OR Name LIKE '%ethnic%'
OR Name LIKE '%gender%'
OR Name LIKE '%french%'
OR Name LIKE '%women%'
OR (Name LIKE '%latin%' AND Name LIKE '%america%')
OR(Name LIKE '%Regional%' AND Name LIKE '%stud%')
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Public Affairs 408
print 'Public Affairs 408'
FieldNum = 408
ConditionStr = '''(
Name LIKE '%Affairs%'
OR Name LIKE '%MPA%'
OR Name LIKE '%Urban%'
OR Name LIKE '%City%'
OR Name LIKE '%estate%'
OR Name LIKE '%MPP%'
OR Name LIKE '%MSW%'
OR Name LIKE '%public Administrat%'
OR(Name LIKE '%Regional%' AND Name NOT LIKE '%stud%')
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Anthropology 409
print 'Anthropology 409'
FieldNum = 409
ConditionStr = '''(
Name LIKE '%Anthropolog%'
OR Name LIKE '%folklore%'
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
OR Name LIKE '%child%'
OR Name LIKE '%teach%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Religion 412
print 'Religion 412'
FieldNum = 412
ConditionStr = '''(
Name LIKE '%Relig%'
OR Name LIKE '%biblical%'
OR Name LIKE '%pastoral%'
OR Name LIKE '%divinity%'
OR Name LIKE '%theology%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Linguistics 413
print 'Linguistics 413'
FieldNum = 413
ConditionStr = '''(
Name LIKE '%Linguistic%'
OR Name LIKE '%language%'
OR Name LIKE '%chinese%'
OR Name LIKE '%japanese%'
OR Name LIKE '%spanish%'
OR Name LIKE '%italian%'
OR Name LIKE '%portuguese%'
OR Name LIKE '%translat%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Literature 414
print 'Literature 414'
FieldNum = 414
ConditionStr = '''(
Name LIKE '%Literature%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Classic 415
print 'Classic 415'
FieldNum = 415
ConditionStr = '''(
Name LIKE '%Classic%'
OR Name LIKE '%greek%'
OR(Name LIKE '%latin%' AND Name NOT LIKE '%america%')
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Criminology 416
print 'Criminology 416'
FieldNum = 416
ConditionStr = '''(
Name LIKE '%Crim%'
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
OR Name LIKE '%Architectur%'
OR Name LIKE '%Design%'
OR Name LIKE '%Art%'
OR Name LIKE '%advertis%'
OR Name LIKE '%media%'
OR Name LIKE '%MFA%'
OR Name LIKE '%theatre%'
OR Name LIKE '%drama%'
OR Name LIKE '%MARch%'
OR Name LIKE '%compos%'
OR Name LIKE '%Film%'
OR Name LIKE '%cinema%'
OR Name LIKE '%jazz%'
OR Name LIKE '%conduct%'
OR Name LIKE '%music%'
OR Name LIKE '%performance%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Public Health 8
print 'Public Health 8'
FieldNum = 8
ConditionStr = '''(
Name LIKE '%Health%'
OR Name LIKE '%Epidemiology%'
OR Name LIKE '%Nutrition%'
OR Name LIKE '%MPH%'
OR Name LIKE '%Food%'
OR Name LIKE '%disease%'
OR Name LIKE '%democracy%'
OR Name LIKE '%recreation%'
OR Name LIKE '%epidemiolog%'
OR Name LIKE '%exercise%'
OR Name LIKE '%kinesiology%'
OR Name LIKE '%dairy%'
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
OR Name LIKE '%resolution%'
OR Name LIKE '%judicial%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Medicine/Medical Science 10
print 'Medical 10'
FieldNum = 10
ConditionStr = '''(
Name LIKE '%Medicine%'
OR Name LIKE '%Pharma%'
OR Name LIKE '%Toxicology%'
OR Name LIKE '%Medical%'
OR Name LIKE '%Immunology%'
OR Name LIKE '%Pathology%'
OR Name LIKE '%nurs%'
OR Name LIKE '%virolog%'
OR Name LIKE '%endocrinology%'
OR Name LIKE '%physiology%'
OR Name LIKE '%counseling%'
OR Name LIKE '%md%'
OR Name LIKE '%therapy%'
OR Name LIKE '%clinical%'
OR Name LIKE '%rehabilitation%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#####################################################
###############           Other         #############
#####################################################

#EngineeringOthers 199
print 'EngineeringOthers 199'
FieldNum = 199
ConditionStr = '''(
Name LIKE '%Engineering%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#ScienceOthers 299
print 'ScienceOthers 299'
FieldNum = 299
ConditionStr = '''(
Name LIKE '%Science%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#BusinessOthers 399
print 'BusinessOthers 399'
FieldNum = 399
ConditionStr = '''(
Name LIKE '%Business%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#SocialOthers 499
print 'SocialOthers 499'
FieldNum = 499
ConditionStr = '''(
Name LIKE '%Social%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

#Undergraduate -1
print 'Undergraduate -1'
FieldNum = -1
ConditionStr = '''(
Name LIKE '%Undergraduate%'
)'''
UpdateDoubleField(FieldNum,ConditionStr)

conn.commit()
cur.close()
conn.close()

