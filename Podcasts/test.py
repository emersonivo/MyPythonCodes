import os
import glob
homedir = os.getcwd()
print (homedir)
# for F in glob.glob(homedir+'/*.txt'):
#     print (F)
#     NewF = str(F).split('.')[0]
#     print ("NewF", NewF)
#     with open(F, 'r') as outF:
#         for line in outF:
#             print (line)
#             if 'bla' in line:
#                 with open(NewF+'.clean', 'a+') as inNewF:
#                     line = line.replace('ble', 'cle').replace('bla', 'fla')
#                     inNewF.write(line)
#     print (NewF)
# ShortLang = ['PX', 'ES', 'EM', 'FR', 'IT', 'DE']
# y = ''
# for L1 in ShortLang:
#     for L2 in ShortLang:
#         if L1 != L2:
#             for x in range(3, 104, 10):
#                 if len(str(x)) == 1:
#                     y = str("00" + str(x))
#                 elif len(str(x)) == 2:
#                     y = str("0" + str(x))
#                 elif len(str(x)) == 3:
#                     y = str(x)
#
#                 print(homedir + "/phrases/" + L1 + L2 + "/" + y)
# with open(homedir+'/Podcasts/podcast101/removecarriage.txt', 'rb') as infile:
#     with open(homedir+'/Podcasts/podcast101/removecarriage.clean', 'a+') as outfile:
#         for line in infile:
#             line = line.replace('\n', '').replace('\r', '')
#             outfile.write(line)

            #/ data / git / MyCodes / Podcasts / podcast101 / removecarriage.txt
dir = glob.glob(homedir+'/Podcasts/podcast101/*.txt')
print('dir', dir)
for file in dir:
    print('file', str(file))
    if file.find('line3'):
        print ("OK")
    else:
        print ("KO")

y = 1
i = ( y * 2 )
print(i)