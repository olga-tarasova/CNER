import codecs
#Extraction chemical entities based on PASS results
dirtory = '' #
filerestsname = "CHEMDNER_1 (2-5)-token.csv" #the directory with input files
fclassesname = "CHEMDNER_1 (2-5)-class.csv"

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
Pa = 0
                                                                                                                                                                                                                                                                 
while i < 404400:
#len(linesrests):
 notadd  = 0
 #CNEx = ""
 linesrests[i] = linesrests[i].replace('"', "")
 linesrests[i] = linesrests[i].replace('  ', "")
 linesrests[i] = linesrests[i].replace(' ', "")
 currsl = linesrests[i].split(";")
 classline = linesclasses[i].split(";")

 if (len(currsl) > 5) and (len(currsl[5]) > 1): 
  try:
   Pa = float(currsl[5][0:len(currsl[5])-1])
  except ValueError:
   print ("valueerror")   
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
    CNEx=""
 if Pa >= threshold: 
  cnecompare = 0
  if cnestart == 1:
   if (currsl[0] in exception_whole) or (currsl[0] in symbols ):
     pass
   else: 
    if (currsl[0] == "(") or (currsl[0] == ")") or (currsl[0] == "-") or (currsl[0] == "-"):
     if classline[0] == 'CNE':
      cnecompare = 1
      TP = TP + 1
     if classline[0] != 'CNE':
      FP = FP + 1 
  if (currsl[0] in exception_whole) or (currsl[0] in symbols )  or (currsl[0].isdecimal() == True) or (currsl[0] == "'s") or (currsl[0] == "@") or (currsl[0] == "*") or (currsl[0] == "''") or (currsl[0] == "``") or (currsl[0] == "[") or (currsl[0] == "]") or (currsl[0] == "+") or (currsl[0] == "-") or (currsl[0] == ">") or (currsl[0] == "'") or (currsl[0] == "{") or (currsl[0] == "}") or (currsl[0] == "(") or (currsl[0] == ")"):
   print ("I am here")
   pass
  else:
   CNEx=CNEx+ " " + currsl[0]
  cnestart = 1
  if (cnecompare == 0):
   cnecompare = 1 
 i = i + 1

print ("FP", FP)
print ("TP", TP)
print ("FN", FN)
print ("TN", TN)
