import os
import shutil
import subprocess
import glob
import json

CONST_NEWLINE = "\n"
CONST_FILENAME = "./out/tempLatex.tex"

def addSubTitle(filef, titleStr):
    filef.write("\\medskip" + CONST_NEWLINE)
    filef.write("\\begin{large}\\textbf{"+ CONST_NEWLINE)
    filef.write(""+ titleStr + CONST_NEWLINE)
    filef.write("}\\end{large}" + CONST_NEWLINE + "\\medskip" + CONST_NEWLINE)

def addTitle(filef, titleStr):
    filef.write("\\medskip" + CONST_NEWLINE)
    filef.write(CONST_NEWLINE+ "\\section{" + titleStr + "}" +CONST_NEWLINE )
    filef.write("\\medskip" + CONST_NEWLINE)

def addContent(filef, descriptionStr):
    filef.write("\\medskip" + CONST_NEWLINE)
    filef.write("$\\bullet$ " + descriptionStr + CONST_NEWLINE)
    filef.write("\\medskip" + CONST_NEWLINE)

def addImage(filef, imageName):
    filef.write("\\medskip" + CONST_NEWLINE)
    filef.write("\\includegraphics[width=\\linewidth]{"+ str(imageName) + "}"  + CONST_NEWLINE)
    filef.write("\\medskip" + CONST_NEWLINE)

def convertLatexToPDF():
    os.system('pdflatex -output-directory ./public/out ' + CONST_FILENAME)
    #os.system('mv tempLatex.pdf out/output.pdf')

def removeImageFolder():
    try:
        shutil.rmtree(dirPath)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))


def createLatexPDF(datas):
    old_files = glob.glob('./out/*')
    for f in old_files:
        os.remove(f)
    old_files = glob.glob('./public/out/*')
    for f in old_files:
        os.remove(f)
    imagePath = "./tempfolder/"

    if os.path.exists(CONST_FILENAME):
        os.remove(CONST_FILENAME)

    filef = open(CONST_FILENAME,"w+")

    with open("top.txt") as f:
        lines = f.readlines()
        lines = [l for l in lines]
        filef.writelines(lines)

    #print(datas)
    for data in datas:
        if(data["tag"] == "highlight"):
            if(data["colour"] == "yellow"):
                addContent(filef, data["text"])
            elif(data["colour"] == "blue"):
                addTitle(filef, data["text"])
            elif(data["colour"] == "pink"):
                addSubTitle(filef, data["text"])
        else:
           addImage(filef, data["index"])




    with open("bot.txt") as f:
        lines = f.readlines()
        lines = [l for l in lines]
        filef.writelines(lines)

    filef.close()
    convertLatexToPDF()


