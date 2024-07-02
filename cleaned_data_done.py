import os
import glob
import re
from cleantext import clean


sample_txt = r"./Data Engineering/data-cleaning/Dirty_logs_text_copy3.txt"
fileName = open('Dirty_logs_text_copy_4.txt', 'r')

lineList = []


def open_documents(filepath):
    filelist = []
    documents = glob.glob(filepath + '/*.txt')
    for i in documents:
        filelist.append(i)
    return filelist


def clean_documents(fileNameAgain):
    # print(fileNameAgain)
    for files in fileNameAgain:
        file = open(files, 'r+')
        file.readline()
        for line in file:
            print("_________________--------------------_____________________-------------------___________________________")
            linecleaned = line[27:]
            # try:
            #     if linecleaned.startswith("+"):
            #         linecleaned = linecleaned[1:]
            #     elif linecleaned.startswith(">"):
            #         linecleaned = linecleaned[1:]
            #     else:
            #         linecleaned = linecleaned
            # except:
            #     pass

            linecleaned = linecleaned.replace("+ ", "")
            linecleaned = linecleaned.replace("> ", "")
            linecleaned = linecleaned.replace("#", "")

            try:
                re.search("(?P<url>https?://[^\s]+)", linecleaned).group("url")
                the_function = clean(
                    linecleaned,
                    fix_unicode=True,
                    to_ascii=True,
                    lower=True,
                    no_numbers=False,
                    # no_digits=True,
                    # no_punct=True,
                    # replace_with_punct="",
                    # replace_with_digit="",
                )

            except:
                the_function = clean(
                    linecleaned,
                    fix_unicode=True,
                    to_ascii=True,
                    lower=True,
                    no_numbers=False,
                    # no_digits=True,
                    no_punct=True,
                    replace_with_punct="",
                    # replace_with_digit="",
                )

            lineList.append(str(the_function)+"\n")
    return lineList


def save_documents(listofLines):
    open('newDocument.txt', 'w+').writelines(listofLines)


firstinput = input("Specify the path of the folder where your txt files are: ")
opened = open_documents(firstinput)
print(type(open))
clean_documents(opened)
save_documents(lineList)
