"""
    Script description:

    This piece of code formats the results for the seasons(2013 - 2015) from the files Output-XXXX(XXXX = 2013 - 2015).
    The result is in ScoreBoard_XXXX.txt which is then converted to .csv file. The csv file will be used for further
    data analysis.

"""

with open("Output-2015.txt", "r") as ins:
    ctr = 0
    s_line = ""
    text_file = open("ScoreBoard_2015.txt", "w")
    for line in ins:
        s_line += line.rstrip("\n") + "   "
        ctr += 1
        print s_line
        if ctr == 3:
            text_file.write(s_line + "\n")
            ctr = 0.
            s_line = ""

#text_file.write("Blah blah")
text_file.close()