import string


"""



"""

map2013 = {}
map2014 = {}
map2015 = {}
mNameTorName13 = set()
mNameTorName14 = set()
mNameTorName15 = set()

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



def removeSquadNumbers():
    # Removing squad numbers
    with open("MatchSquads-2015_final.txt", "r") as fin, open("MatchSquads_2015-final.txt", "w") as fout:
        for line in fin:
            var = str(line)
            var = var.rstrip('\n')
            if "Positions" not in var and "END,MATCH" not in var and "NEXT,TEAM" not in var and "..." not in var and "Substitutes" not in var:
                x = var.split(',')
                x.pop(0)
                new_var = ""
                for y in x:
                    if new_var == "":
                        new_var = y
                    else:
                        new_var = new_var + "," + y
                fout.write(new_var + '\n')
            else:
                fout.write(var + '\n')

    fin.close()
    fout.close()


def identifyPlayerNames():
    with open("MatchSquads_2015-final.txt","r") as fin, open("MatchSquads-2015_final.txt","w") as fout:
        for line in fin:
            var = str(line)
            var = var.rstrip('\n')
            if "Positions" not in var and "END,MATCH" not in var and "NEXT,TEAM" not in var and "..." not in var and "Substitutes" not in var:
                x = var.split(',')
                new_var = ""
                for y in x:
                    if "'" not in y and "Goalkeeper" not in y and "Defender" not in y and "Midfielder" not in y and "Forward" not in y:
                        if new_var == "":
                            new_var = new_var + y
                        else:
                            new_var = new_var + " " + y
                    else:
                        new_var = new_var + "," + y
                fout.write(new_var + '\n')
            else:
                fout.write(var + '\n')



def loadPlayerRatings(text_file):
    """

    :param text_file:
    :return:
    Function description: This function loads all the player ratings of a given year into a map, where the
    key is the team name and the value is the player name and rating.
    """
    global map2013
    global map2014
    global map2015

    with open(text_file,"r") as fin:
        for line in fin:
            x = line.split(',')
            map2013[x[1]] = [x[0],x[2],x[3]]


    fin.close()
    cnt = 0
    for i in map2013:
        cnt += 1
        #print i,map2013[i]

    #print cnt


def digInString(var):
    return any(char.isdigit() for char in var)


def editDistDP(str1, str2, m, n):
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # Min. operations = j
            elif j == 0:
                dp[i][j] = i  # Min. operations = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]


def getMatch(name,team):
    ret = ""
    if name not in mNameTorName13:
        mn = 10000000
        for i in map2013:
            if team == map2013[i][0]:
                temp = editDistDP(name, i, len(name),len(i))
                if temp < mn:
                    mn = temp
                    ret = i

        mNameTorName13.add(i)

    return ret






def calculateMatchRatings(text_file):
    cur_team = ""
    cur_team_def_rating = 0
    cur_team_mid_rating = 0
    cur_team_att_rating = 0
    cur_team_rating = 0
    starting_eleven_cnt = 0
    with open(text_file,"r") as fin:
        for line in fin:
            var = str(line)
            var = var.rstrip('\n')
            if "Positions" in var:
                x = var.split(',')
                cur_team = x[0]
                starting_eleven_cnt = 0
                print cur_team

            elif "Positions" not in var and "END,MATCH" not in var and "NEXT,TEAM" not in var and "..." not in var and "Substitutes" not in var:
                substitute = digInString(var)
                starting_eleven_cnt += 1
                if starting_eleven_cnt < 11:
                    x = var.split(',')
                    temp_name = x[0]
                    temp_name = temp_name.split(' ')
                    #print temp_name
                    if temp_name[-1] == "90" or temp_name[-1] == "45":
                        temp_name.pop()

                    fin_name = " ".join(temp_name)
                    #print fin_name
                    playerName = getMatch(fin_name,cur_team)
                    print playerName, map2013[playerName][1]

                elif substitute == True:
                    x = var.split(',')
                    temp_name = x[0]
                    temp_name = temp_name.split(' ')
                    # print temp_name
                    if temp_name[-1] == "90" or temp_name[-1] == "45":
                        temp_name.pop()

                    fin_name = " ".join(temp_name)
                    #print fin_name
                    playerName = getMatch(fin_name,cur_team)
                    print playerName, map2013[playerName][2]




#Text file open
#ratings_file = open("PlayerRatings-2013-Final.txt","r")

#cleanFile("MatchSquads-2015.txt")
#removeSquadNumbers()
#identifyPlayerNames()
loadPlayerRatings("PlayerRatings-2013-Final.txt")
calculateMatchRatings("MatchSquads-2013_final.txt")