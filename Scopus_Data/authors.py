import pyscopus
from pyscopus import Scopus
import pandas as pd

key='bc87ef89794f6f531edb4162d12d3e7e'
scopus = Scopus(key)
subject_area=["SUBJAREA(AGRI)","SUBJAREA(BIOC)","SUBJAREA(BUSI)","SUBJAREA(CENG)","SUBJAREA(CHEM)","SUBJAREA(COMP)","SUBJAREA(DECI)","SUBJAREA(PHAR)","SUBJAREA(MULT)",
"SUBJAREA(VETE)","SUBJAREA(SOCI)","SUBJAREA(PSYC)","SUBJAREA(NURS)","SUBJAREA(NEUR)","SUBJAREA(DENT)","SUBJAREA(EART)","SUBJAREA(ECON)","SUBJAREA(ENER)","SUBJAREA(ENGI)","SUBJAREA(ENVI)",
"SUBJAREA(HEAL)","SUBJAREA(MATH)","SUBJAREA(IMMU)","SUBJAREA(MATE)","SUBJAREA(MEDI)","SUBJAREA(PHYS)"]


authors=pd.DataFrame(columns=['author_id','name','affiliation_id'])

for subj in subject_area:
    try:
        author_search_df = scopus.search_author(subj,count=2500)
        author_search_df=author_search_df[['author_id','name','affiliation_id']]
        authors=authors.append(author_search_df).drop_duplicates()
        print(authors)
        authors.to_csv('authors.csv',index=False)
    except :
        pass
    
    





