

#Extraction chemical entities based on PASS results
dirtory = 'D:\\Texts\\PASS-rests\\'
f=open(dirtory + "MproSW_results_1.txt", 'r')
lines = f.readlines()
threshold = 0.35
CNEx = ""
i = 1
chemlist = []
FP = 0
EasyFP = 0
notadd = 0
exceptions = ['<', '>', "'s", '``']
exception_whole = ['(', ')', "'", '+', '@', '[', ']', '``', ') (', '] [', '{', '}',
                    'Δ', 'δ', 'Ⅰ', 'α', 'β', '˂γ˃', 'ε', '…', 'ω', 'η', 'III', 'iii', 'N°' 'named', 'cycle',
                    'nine', 'bonds', 'obeys', '3CL', 'myriad', 'mine', 'Nine', 'done', 'CID', 'ones', 'Z', 'curb',
                    'N3', 'Xa', 'none', 'palm', 'Amazon', 'bond', 'None', 'cyclic', '\u200b\u200bof', 'iDock',
                    'and', 'Pro', '3CL Pro', '3CL-Pro', 'protein', 'on', 'then', 'with', 'were', 'in', 'an', 'than',
                    'when', 'of', 'then', 'or', 'to', 'the', 'natural', 'dye', 'administration',  "'s", "@", "*", "''", "``", "[", "]", "+", "-", ">", "'", "{", "}", "(", ")"]
symbols = ['-', "'", '·', '+', '``', "''", 'Ⅰ', '=', '˙', '~']

#print (len (lines))                                                                                                                                                                                                                                                                   
while i < len (lines):
 notadd  = 0
 #CNEx = ""
 lines[i] = lines[i].replace('"', "")
 lines[i] = lines[i].replace('  ', "")
 lines[i] = lines[i].replace(' ', "")
 currsl = lines[i].split(",")
 #print (currsl)
 if (len(currsl) > 5) and (len(currsl[5]) > 1): 
  try:
   Pa = float(currsl[5][0:len(currsl[5])-1])
  except ValueError:
 #  print ("valueerror")   
 #print (Pa)
 if Pa < threshold:
  if CNEx != "":
    testCNE = 
  # if notadd == 0:
  #первый символ +
    CNEx = CNEx.replace("- ", "-")
    CNEx = CNEx.replace(" -", "-")
    CNEx = CNEx.replace("=+", "")
    CNEx = CNEx.replace(" (", "(")
    CNEx = CNEx.replace(" )", ")")
    testCNE = CNEx.replace("-", "")
    testCNE = CNEx.replace(".", "")
    testCNE = CNEx.replace(".", "")
    if CNEx[len(CNEx)-1] == "(":
     CNEx = CNEx[0:len(CNEx)-2]
    if len(CNEx) > 1:
     chemlist.append(CNEx + "\n")
   # print (CNEx)
    CNEx=""
   # notadd=0
 if Pa >= threshold:
  if (currsl[0].isdecimal() == True) or (currsl[0] in exception_whole) or (currsl[0] in symbols ):
   FP = FP + 1
   EasyFP = EasyFP + 1
  # notadd = 1
  else:
   if len(CNEx) > 0:
    CNEx=CNEx+ " " + currsl[0]
   else:
    CNEx = currsl[0]
 # notadd = 0
 i = i + 1

#print (FP)
#print (EasyFP)
file = open(dirtory + "outchemlist-Mpro-2104-thresh-030.txt", 'w')
file.writelines(chemlist)
file.close()
