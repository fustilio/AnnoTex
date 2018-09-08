import os
import shutil
import subprocess
import json

CONST_NEWLINE = "\n"
CONST_FILENAME = "tempLatex.tex"

def addSubTitle(filef, titleStr):
    filef.write("\\underline{\\begin{large}\\textbf{"+ CONST_NEWLINE)
    filef.write(titleStr + CONST_NEWLINE)
    filef.write("}\\end{large}}" + CONST_NEWLINE + "\\newline" + CONST_NEWLINE)

def addTitle(filef, titleStr):
     filef.write(CONST_NEWLINE+ "\\section{" + titleStr + "}" +CONST_NEWLINE )

def addContent(filef, descriptionStr):
    filef.write("$\\bullet$ " + descriptionStr + CONST_NEWLINE)
    filef.write("\\newline" + CONST_NEWLINE)

def convertLatexToPDF():
    subprocess.call('pdflatex ' + CONST_FILENAME)

def removeImageFolder():
    try:
        shutil.rmtree(dirPath)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))


def createLatexPDF(datas): 
    imagePath = "./tempfolder/"

    if os.path.exists(CONST_FILENAME):
        os.remove(CONST_FILENAME)

    filef = open(CONST_FILENAME,"w+")

    with open("top.txt") as f:
        lines = f.readlines()
        lines = [l for l in lines]
        filef.writelines(lines)


    for data in datas:
        if(data["tag"] == "highlight"):
            if(data["colour"] == "yellow"):
                addContent(filef, data["text"])
            elif(data["colour"] == "blue"):
                addTitle(filef, data["text"])
            elif(data["colour"] == "pink"):
                addSubTitle(filef, data["text"])



    with open("bot.txt") as f:
        lines = f.readlines()
        lines = [l for l in lines]
        filef.writelines(lines)

    filef.close()
    convertLatexToPDF()


