import urllib.request as ull
import urllib
import codecs
filename = 'filepath'
file = codecs.open(filepath, 'r', encoding = 'utf-8')
lines = file.readlines()
chemicals = []
filename_w = 'filepath_w'
f = codecs.open(filename_w, 'a', encoding = 'utf-8')
count = 1
for line in lines:
    print(str(count) + '/' + str(len(lines)))
    count = count +1
    if line[:-2].lower() not in chemicals:
        chemicals.append(line[:-2].lower())
        crn = line[:-2]
        crn = crn.replace('\\' , '-')
        crn = crn.replace(' ' , '%20')
        try:
            chembl = urllib.request.urlopen("https://www.ebi.ac.uk/chembl/api/data/molecule/search?q=" + crn)
            data_id = str(chembl.read())
            start_id = data_id.find("<molecule_chembl_id>")
            if start!=-1:
                chembl_status = 1
            else:
                chembl_status = 0
        except:
            chembl_status = 0
        try:
            pubchem = urllib.request.urlopen("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/" + crn)
            ##c
            pubchem_status = 1
            print('PubChem есть')
        except:
            pubchem_status = 0
            print('PubChem нет')
        f.write(line[:-2].lower() + '\t' + str(chembl_status) + '\t' + str(pubchem_status) + '\n')
f.close()

