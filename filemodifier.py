import os
print('Python file type changer / renamer V1.0')
print('Drag 1 of the files to be renamed in here to get the file path and press enter:')
path1 = input()
print('Rename files? Default: False, enter anything for True')
rename = str(input('rename to: '))
print('change to which filetype? jpeg, png, txt etc.')
filetype = input() #Example: "C:\Users\Admin\Desktop\New folder\jeg.png"
path1 = path1.replace("'",'')
path1 = path1.replace('"','')
stringpath = ''
if os.path.isfile(path1):
    if '\\' in path1:
        path1 = path1.split('\\')
        del path1[-1] #Removes file name to get only path
        for item in path1:
            stringpath = stringpath + item + '\\'
        print(stringpath)
    elif '/' in path1:
        print('found 2')
        path1 = path1.split('/')
        del path1[-1] #Removes file name to get only path
        for item in path1:
            stringpath = stringpath + item + '/'
elif os.path.isdir(path1):
    if path1[-1] == '/' or path1[-1] == '\\':
        stringpath = path1
    else:
        if '\\' in path1:
            path1.replace('\\', '/')
        stringpath = path1 + '/'
else:
    print('Error: wrong path. \n Example use: C:\\Users\\Brian\\Desktop\\testfolder\\photo.png \n or C:/Users/Brian/Desktop/testfolder')

filelist = os.listdir(stringpath)
filelistlen = len(filelist)
print('[',filelistlen,'] Files found in',stringpath)
counter = 0
if rename == '':
    if filelistlen > 100:
        for item in filelist:
            itempart = item.partition('.')
            os.rename(stringpath + item, stringpath + itempart[0] + '.' + filetype)
            if counter % 100 == 0:
                pdone = round((counter / filelistlen)*100,0)
                print('[',pdone,'%] complete.', counter,'/',filelistlen)

            counter += 1
            if counter == filelistlen:
                print('[ 100 %] complete.', filelistlen, '/', filelistlen)
    else:
        for item in filelist:
            itempart = item.partition('.')
            os.rename(stringpath + item, stringpath + itempart[0] + '.' + filetype)
        print('Task complete.')
else:
    namecount = 1
    if filelistlen > 100:
        for item in filelist:
            os.rename(stringpath + item, stringpath + rename + str(namecount) + '.' + filetype)
            namecount += 1
            if counter % 100 == 0:
                pdone = round((counter / filelistlen) * 100, 0)
                print('[', pdone, '%] complete.', counter, '/', filelistlen)

            counter += 1
            if counter == filelistlen:
                print('[ 100 %] complete.', filelistlen, '/', filelistlen)
    else:
        for item in filelist:
            os.rename(stringpath + item, stringpath + rename + str(namecount) + '.' + filetype)
            namecount += 1
        print('Task complete.')
