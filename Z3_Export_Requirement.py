import MySQLdb
import Config
import json

Listall = []

conn=MySQLdb.connect(host=Config.host,user=Config.user,passwd=Config.passwd,port=Config.port,db=Config.db,charset=Config.charset)
cur=conn.cursor()
str1 = "SELECT \
ApplicationFeeHas,ApplicationFee,ApplicationFeeType,ApplicationFeeOrigin,\
ToeflHas,ToeflIBTTotal,ToeflIBTReading,ToeflIBTListening,ToeflIBTSpeaking,ToeflIBTWriting,ToeflIBTOrigin,ToeflIBTNote,\
IeltsHas,IeltsTotal,IeltsReading,IeltsListening,IeltsSpeaking,IeltsWriting,IeltsOrigin,IeltsNote,\
GreHas,GreTotal,GreVerbal,GreQuantitative,GreWriting,GreOrigin,GreNote,DegreeRequireHas,DegreeRequire,CourseRequire,MajorRequire,\
TranscriptHas,TranscriptNote,TranscriptOringin,PsHas,PsOrigin,PsNote,ResumeHas,ResumeOrigin,ResumeNote,\
RecommendationHas,RecommendationNum,RecommendationOrigin,WorkExpHas,WorkExpOrigin,ProjectExpHas,ProjectExpOrigin,\
SATorACTHas,SATorACTOrigin,SATsubjecttestsHas,SATsubjecttestsOrigin,APExamsHas,APExamsOrigin,WritingSampleHas,WritingSampleNote,\
TeacherEvaluationsHas,TeacherEvaluationsNote,SchoolReportHas,SchoolReportNote,ScoreChoiceHas,ScoreChoiceOrigin,\
InternationalStudentNoticeHas,InternationalStudentNoticeOrigin,Id \
FROM programinstance"

cur.execute(str1)
result = cur.fetchall()
for i in result:

    dic = {
        'ApplicationFeeHas':i[0],
        'ApplicationFee':i[1],
        #'ApplicationFeeType':i[2],'ApplicationFeeOrigin':i[3],
        'ToeflHas':i[4],'ToeflIBTTotal':i[5],
        #'ToeflIBTReading':i[6],'ToeflIBTListening':i[7],'ToeflIBTSpeaking':i[8],'ToeflIBTWriting':i[9],'ToeflIBTOrigin':i[10],'ToeflIBTNote':i[11],
        'IeltsHas':i[12],'IeltsTotal':str(i[13]),
        #'IeltsReading':str(i[14]),'IeltsListening':str(i[15]),'IeltsSpeaking':str(i[16]),'IeltsWriting':str(i[17]),'IeltsOrigin':i[18],'IeltsNote':i[19],
        'GreHas':i[20],'GreTotal':i[21],
        #'GreVerbal':i[22],'GreQuantitative':i[23],'GreWriting':str(i[24]),'GreOrigin':i[25],'GreNote':i[26],'DegreeRequireHas':i[27],'DegreeRequire':i[28],'CourseRequire':i[29],'MajorRequire':i[30],
        'TranscriptHas':i[31],
        #'TranscriptNote':i[32],'TranscriptOringin':i[33],
        'PsHas':i[34],
        #'PsOrigin':i[35],'PsNote':i[36],
        'ResumeHas':i[37],
        #'ResumeOrigin':i[38],'ResumeNote':i[39],
        'RecommendationHas':i[40],'RecommendationNum':i[41],#'RecommendationOrigin':i[42],'WorkExpHas':i[43],'WorkExpOrigin':i[44],'ProjectExpHas':i[45],'ProjectExpOrigin':i[46],
        'SATorACTHas':i[47],
        #'SATorACTOrigin':i[48],
        'SATsubjecttestsHas':i[49],#'SATsubjecttestsOrigin':i[50]
        'APExamsHas':i[51],
        #'APExamsOrigin':i[52],
        'WritingSampleHas':i[53],
        #'WritingSampleNote':i[54],
        'TeacherEvaluationsHas':i[55],
        #'TeacherEvaluationsNote':i[56],
        'SchoolReportHas':i[57],
        #'SchoolReportNote':i[58],
        'ScoreChoiceHas':i[59],
        #'ScoreChoiceOrigin':i[60],
        #'InternationalStudentNoticeHas':i[61],'InternationalStudentNoticeOrigin':i[62],
        'programInstanceId':i[63]
    }
    Listall.append(dic)

jsonStr = json.dumps(Listall);

file_object = open('ProgramInstanceRequirements.json', 'w')
file_object.write(jsonStr)
file_object.close()

cur.close()
conn.close()
