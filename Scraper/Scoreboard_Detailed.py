import csv
from collections import OrderedDict

"""

Script Description:



"""

def addStats(val,matchId):
    myList = [item for item in val.split('\n')]
    newString = ''.join(myList)
    #print matchId
    statsList[matchId] = newString

statsList = OrderedDict()

with open("Stats-2013.txt","r") as ins:
    # print "A" + cnt
    cnt = 0
    val = ","
    matchId = ""
    for line in ins:
        # print cnt
        rVal = str(line)
        x = rVal.split(',')
        #print x
        if cnt == 0:
            cnt += 1
            #val = val + x[1] + ","
            #print x[1].rstrip('\n')
            matchId = x[1].rstrip('\n')
            #print matchId
        else:
            val = val + x[0] + "," + x[2] + ","
            #print x[0] + "," + x[2] + ",".rstrip('\n')
            cnt += 1
            if cnt == 10:
                #print val
                addStats(val,matchId)
                val = ","
                cnt = 0
                #break


#for i in statsList:
#    print i, statsList[i]
text_file = open("ScoreBoard_Detailed_2013.txt","w")
with open("ScoreBoard_2013.txt","r") as ins:
    idx = 0
    for line in ins:
        value_at_index = statsList.values()[idx]
        key_at_index = statsList.keys()[idx]
        val = str(line).rstrip('\n')
        val = key_at_index + "," + val
        val = val + "," + value_at_index
        val = val.rstrip(',')
        #print val
        text_file.write(val + '\n')
        idx += 1

text_file.close()


