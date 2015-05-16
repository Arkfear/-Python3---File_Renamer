#encoding = utf-8
import os
from os import listdir
from os.path import isfile, join

path = os.path.dirname(os.path.realpath(__file__))

onlyfiles = [ f for f in listdir(path) if isfile(join(path,f))]
#onlyfiles = listdir(path)
for files in onlyfiles:
    if(files[0]!='.'):
        basefilename, ext = os.path.splitext((files))
        ext = ext.lower()
        os.rename(files,basefilename+ext)
        print(basefilename,ext)
