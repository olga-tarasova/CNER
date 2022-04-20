import codecs
#Extraction chemical entities based on PASS results
dirtory = 'D:\\Texts\\CHEMDNER_5_FOLD\\CNE_test\\'
filerestsname = "CHEMDNER_5 (1_string5_chemdner1-4)-target-token-determined-csv.txt"
fclassesname = "CHEMDNER_5 (1_string5_chemdner1-4)-target-token-class.csv"

#frests=open(dirtory + filerests_name, 'r') #открываем CSV с результатами
#linesrests = frests.readlines()

#fclasses=open(dirtory + fclasses_name, 'r')  #открываем CSV с принадлежностью к классу
#linesclasses = fclasses.readlines()

frests = codecs.open(dirtory + filerestsname, 'r', 'utf-8', errors = 'replace')  #открываем CSV с результатами
linesrests = frests.readlines()

fclasses = codecs.open(dirtory + fclassesname, 'r', 'utf-8', errors = 'replace')  #открываем CSV с принадлежностью к классу
linesclasses = fclasses.readlines()

threshold = 0.30
CNEx = ""
i = 9
chemlist = []
FP = 0
EasyFP = 0
notadd = 0
cnestart = 0
cnecompare = 0
tokenFP = 0
tokenFN = 0
tokenTP = 0
tokenTN = 0
FP = 0
FN = 0
TP = 0
TN = 0

exception_whole = ['(', ')', "'", '+', '@', '[', ']', '``', ') (', '] [', '{', '}', 'named', 'cycle', 'Δ', 'δ', 'Ⅰ', 'α', 'β', '˂γ˃', 'ε',
                'nine', 'bonds', 'obeys', '3CL', 'myriad', 'mine', 'Nine', 'done', 'III', 'iii', 'CID', 'ones', 'Z',
                'curb', 'N3', 'Xa', 'none', 'palm', 'Amazon', 'bond', 'None', 'cyclic', '\u200b\u200bof', 'iDock', '…',
                'ω', 'η', 'and', 'Pro', '3CL Pro', '3CL-Pro', 'protein', 'on', "then", "with", "were"]
symbols = ["'", '·', '+', '``', "''", 'Ⅰ', '=', '˙', "+-", "(-"]
#Pa = 0
print (len (linesrests))
print (len (linesclasses))                                                                                                                                                                                                                                                                   
while i < len (linesrests):
 notadd  = 0
 #CNEx = ""
 linesrests[i] = linesrests[i].replace('"', "")
 linesrests[i] = linesrests[i].replace('  ', "")
 linesrests[i] = linesrests[i].replace(' ', "")
 currsl = linesrests[i].split(";")
 classline = linesclasses[i].split(";")
 #print (currsl)
 if (len(currsl) > 5) and (len(currsl[5]) > 1): 
  try:
   Pa = float(currsl[5][0:len(currsl[5])-1])
  except ValueError:
   print ("valueerror")   
# print (Pa)
 if Pa < threshold:
  if classline[0] != 'CNE':
   TN = TN + 1
  else:
   FN = FN + 1  
  #if cnestart == 0:
   #TN = TN + 1 
  if cnestart == 1:
   if classline[0] == 'CNE':
    TP = TP + 1
  # if cnecompare == 0:
   # FN = FN + 1
  cnestart = 0
  if CNEx != "":
  # if notadd == 0:
  #первый символ +
    CNEx = CNEx.replace("- ", "-")
    CNEx = CNEx.replace(" -", "-")
    CNEx = CNEx.replace("=+", "")
    if CNEx[len(CNEx)-1] == "(":
     CNEx = CNEx[0:len(CNEx)-2]
    if len(CNEx) > 1:
     chemlist.append(CNEx + "\n")
  #  print (CNEx)
    CNEx=""
   # notadd=0
 if Pa >= threshold: 
  cnecompare = 0
  if cnestart == 1:
   if (currsl[0] in exception_whole) or (currsl[0] in symbols ):
     pass
     #CNEx=CNEx+ " " + currsl[0]
     #print (classline[0])
   else: 
    if (currsl[0] == "(") or (currsl[0] == ")") or (currsl[0] == "-") or (currsl[0] == "-"):
     if classline[0] == 'CNE':
      cnecompare = 1
      TP = TP + 1
     #else:
      #cnecompare = 0
     if classline[0] != 'CNE':
      FP = FP + 1
    #else:
     #if (currsl[0] in exception_whole) or (currsl[0] in symbols ):
     # FP = FP + 1    
  #if cnestart == 0:  
  if (currsl[0] in exception_whole) or (currsl[0] in symbols )  or (currsl[0].isdecimal() == True) or (currsl[0] == "'s") or (currsl[0] == "@") or (currsl[0] == "*") or (currsl[0] == "''") or (currsl[0] == "``") or (currsl[0] == "[") or (currsl[0] == "]") or (currsl[0] == "+") or (currsl[0] == "-") or (currsl[0] == ">") or (currsl[0] == "'") or (currsl[0] == "{") or (currsl[0] == "}") or (currsl[0] == "(") or (currsl[0] == ")"):
   # TN = TN + 1
   print ("I am here")
   pass
   # FP = FP + 1
   # EasyFP = EasyFP + 1
    # notadd = 1
  else:
   CNEx=CNEx+ " " + currsl[0]
 # if (cnestart == 0):
  cnestart = 1
  if (cnecompare == 0):
   cnecompare = 1 
 # notadd = 0
 i = i + 1

print (FP)
print (TP)
print (FN)
print (TN)
#print (FP)
fout = codecs.open(dirtory + "outchemlist.txt", 'w', 'utf-8', errors = 'replace') 
#file = open(dirtory + "outchemlist-Mpro-3103-thresh-03.txt", 'w')
fout.writelines(chemlist)
fout.close()
