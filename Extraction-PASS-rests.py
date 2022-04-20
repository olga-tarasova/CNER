

#Extraction chemical entities based on PASS results
dirtory = 'E:\\Texts\\PASS-rests\\'
f=open(dirtory + "MproSW_results.csv", 'r')
lines = f.readlines()
threshold = 0.30
CNEx = ""
i = 1
chemlist = []
FP = 0
EasyFP = 0
notadd = 0
print (len (lines))                                                                                                                                                                                                                                                                   
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
   print ("valueerror")   
 print (Pa)
 if Pa < threshold:
  if CNEx != "":
  # if notadd == 0:
  #первый символ +
    CNEx = CNEx.replace("- ", "-")
    CNEx = CNEx.replace(" -", "-")
    CNEx = CNEx.replace("=+", "")
    CNEx = CNEx.replace(" (", "(")
    CNEx = CNEx.replace(" )", ")")
    if CNEx[len(CNEx)-1] == "(":
     CNEx = CNEx[0:len(CNEx)-2]
    if len(CNEx) > 1:
     chemlist.append(CNEx + "\n")
    print (CNEx)
    CNEx=""
   # notadd=0
 if Pa >= threshold:
  if (currsl[0].isdecimal() == True) or (currsl[0] == "'s") or (currsl[0] == "@") or (currsl[0] == "*") or (currsl[0] == "''") or (currsl[0] == "``") or (currsl[0] == "[") or (currsl[0] == "]") or (currsl[0] == "+") or (currsl[0] == "-") or (currsl[0] == ">") or (currsl[0] == "'") or (currsl[0] == "{") or (currsl[0] == "}") or (currsl[0] == "(") or (currsl[0] == ")"):
   FP = FP + 1
   EasyFP = EasyFP + 1
  # notadd = 1
  else:
   CNEx=CNEx+ " " + currsl[0]
 # notadd = 0
 i = i + 1

print (FP)
print (EasyFP)
file = open(dirtory + "outchemlist-Mpro-3103-thresh-03.txt", 'w')
file.writelines(chemlist)
file.close()
