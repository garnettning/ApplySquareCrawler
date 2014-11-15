listfile=[]
listfile.append('USNews')
listfile.append('LiberalArts')
listfile.append('QS')
listfile.append('TIMES')
listfile.append('usnews_school_engineering')
listfile.append('usnews_school_law')
listfile.append('usnews_school_business')
listfile.append('usnews_school_medical_primary_care')
listfile.append('usnews_school_medical_research')
listfile.append('usnews_school_fine_arts')

listall=[]

x=0
for i in listfile:
    x=x+1
    print '***  No.%d   ***'%x
    filename = 'Zinfo_'+i+'_List.txt'
    file_object = open(filename)
    List = file_object.readlines()
    file_object.close()
    for j in List:
        if j not in listall:
            listall.append(j)

file_object = open('Zinfo_Alluniversity_List.txt', 'w')
file_object.writelines(listall)
file_object.close()

for i in listall:
    print i
print len(listall)
