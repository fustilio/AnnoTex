import os
import shutil
import subprocess
import glob
import json
import re

CONST_NEWLINE = "\n"
CONST_FILENAME = "./out/tempLatex.tex"

def escapeSymbols(str):
    conv = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
        '<': r'\textless{}',
        '>': r'\textgreater{}',
    }
    regex = re.compile('|'.join(re.escape(unicode(key)) for key in sorted(conv.keys(), key = lambda item: - len(item))))
    return regex.sub(lambda match: conv[match.group()], str)



def addTitle(filef, titleStr):
    titleStr = escapeSymbols(titleStr)
    filef.write(CONST_NEWLINE+ "\\section{" + titleStr.encode('utf-8') + "}" +CONST_NEWLINE )


def addSubTitle(filef, titleStr):
    titleStr = escapeSymbols(titleStr)
    filef.write("\\begin{large}\\textbf{"+ CONST_NEWLINE)
    filef.write(""+ titleStr.encode('utf-8')+ CONST_NEWLINE)
    filef.write("}\\end{large}" + CONST_NEWLINE + "\\newline" + CONST_NEWLINE)

def addContent(filef, descriptionStr):
    descriptionStr = escapeSymbols(descriptionStr)
    filef.write("$\\bullet$ " + descriptionStr.encode('utf-8') + CONST_NEWLINE)
    filef.write("\\newline" + CONST_NEWLINE)


def addImage(filef, imageName):
    filef.write("\\includegraphics[width=\\linewidth]{"+ str(imageName) + "}"  + CONST_NEWLINE)
    filef.write("\\newline" + CONST_NEWLINE)


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
            text = data["text"][1:-1]
            text = text.replace(text[0], text[0].upper(), 1)
            if(data["colour"] == "yellow"):
               addContent(filef, text)
            elif(data["colour"] == "blue"):
                 addTitle(filef, text)
                
            elif(data["colour"] == "pink"):
                addSubTitle(filef, text)
        else:
           addImage(filef, data["index"])





    with open("bot.txt") as f:
        lines = f.readlines()
        lines = [l for l in lines]
        filef.writelines(lines)

    filef.close()
    convertLatexToPDF()


