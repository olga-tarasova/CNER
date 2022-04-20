import os
import urllib.request as ull
import urllib as ul
import codecs
dirtory = 'D:\\Texts\\PASS-rests\\'
with codecs.open(dirtory + "out-chemlist-SARS-CoV-2.txt", encoding = "utf8") as f:
 lines = f.readlines()
#lines = 
i=1
k=0
n=0
found = 1
outlist = []
while i < len(lines):
 currsl = lines[i].split("\t")
 crn =  currsl[0]
 crn = crn.replace('\\' , '-')
 crn = crn.replace(' ' , '%20')
 crn = crn.lower()
 print (crn)
 found = 1
 try:
  ull.urlretrieve ('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/' + crn + '/XML/', dirtory + "temp" + ".xml")
  print("found")
    #    ull.urlretrieve ('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/synonyms/hereisis/XML/', dirtory + "1-energy" + ".xml")
 except ul.error.HTTPError:
  print ("not found")
  found = 0
 except UnicodeEncodeError:
  print ("Encode Error")
  found = 2
    #ull.urlretrieve ('https://www.ebi.ac.uk/chembl/api/data/similarity/CC1=CN([C@H]2C[C@H](N=[N+]=[N-])[C@@H](CO)O2)C(=O)NC1=O/100', dirtory + "1" + ".xml")
	#ull.urlretrieve('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&rettype=abstract&retmode=text&id=' + s, dirtory + s + ".txt")
	#ull.urlretrieve ('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&rettype=abstract&retmode=xml&id=' + s, dirtory + s + ".xml")
	 #k=0
 outlist.append(str(found)+ "   " + lines[i])
 i=i+1

file = open(dirtory + "outpubchemlist_SARS-CoV-2-drugs.txt", 'w')
file.writelines(outlist)
file.close()

# 
