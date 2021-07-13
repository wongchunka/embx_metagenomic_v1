from xml.dom import minidom
import os, glob 
import pandas as pd

# setting
dir_in = "path1"
path_out =  "path2/output.csv"

# execution
xml = glob.glob(os.path.join(dir_in, "*.xml"))
ls_title = []
ls_length = []
ls_virus_tax = []
ls_virus_name = []
ls_evalue = []
ls_perciden = []

for xml_f in xml:
    xml_p = minidom.parse(xml_f)
    search = xml_p.getElementsByTagName('Search')
    for s in search:
        title = s.getElementsByTagName('query-title')[0].childNodes[0].data
        length = s.getElementsByTagName('query-len')[0].childNodes[0].data
        try:
            hit = s.getElementsByTagName('Hit')[0]
            virus_name = hit.getElementsByTagName('description')[0].getElementsByTagName('HitDescr')[0].getElementsByTagName('title')[0].childNodes[0].data
            virus_tax = hit.getElementsByTagName('description')[0].getElementsByTagName('HitDescr')[0].getElementsByTagName('taxid')[0].childNodes[0].data
            evalue = hit.getElementsByTagName('Hsp')[0].getElementsByTagName('evalue')[0].childNodes[0].data
            perciden = 100*int(hit.getElementsByTagName('Hsp')[0].getElementsByTagName('identity')[0].childNodes[0].data) / int(hit.getElementsByTagName('Hsp')[0].getElementsByTagName('align-len')[0].childNodes[0].data)
            ls_title.append(title)
            ls_length.append(length)
            ls_virus_tax.append(virus_tax)
            ls_virus_name.append(virus_name)
            ls_evalue.append(evalue)
            ls_perciden.append(perciden)
            print(title, length, 'Hit found', virus_tax, virus_name, evalue)
        except:
            print(title, length, 'Hit not found')

df = pd.DataFrame({
    'title': ls_title,
    'length': ls_length,
    'virus_tax': ls_virus_tax,
    'virus_name': ls_virus_name,
    'evalue': ls_evalue,
    'perciden': ls_perciden
})

df.to_csv(path_out, index=False)
