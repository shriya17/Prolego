import string

"""

This

"""

def cleanFile(text_file):
    with open(text_file,"r") as fin, open("MatchSquads-2015_final.txt","w") as fout:
        flag = 0
        temp = ""
        for line in fin:
            var = str(line)
            var = var.rstrip('\n')
            if "Positions" not in var and "END MATCH" not in var and "NEXT TEAM" not in var and "..." not in var and "Substitutes" not in var:
                if flag == 0:
                    temp = ""
                    temp += var
                    flag = 1
                elif flag == 1:
                    if "Goalkeeper" in var or "Defender" in var or "Midfielder" in var or "Forward" in var:
                        temp = temp + " " + var
                        flag = 0
                        fout.write(temp + '\n')
                    else:
                        temp = temp + " " + var
            else:
                fout.write(var + '\n')

    fin.close()
    fout.close()


#Text file open
#ratings_file = open("PlayerRatings-2013-Final.txt","r")
cleanFile("MatchSquads-2015.txt")

#Removing squad numbers
with open("MatchSquads-2013_final.txt","r") as fin:
    for line in fin:
        var = str(line)
