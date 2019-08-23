import pyscopus
from pyscopus import Scopus
import pandas as pd

key='bc87ef89794f6f531edb4162d12d3e7e'
scopus = Scopus(key)

authors = pd.read_csv("authors.csv")

affiliations_id=authors['affiliation_id'].values
affiliations=pd.DataFrame(columns=['affiliation-name','city','country','aff_id'])

print(len(affiliations_id))
for aff in affiliations_id:
    try:
        affiliation=scopus.retrieve_affiliation(str(int(aff)))
        affil=pd.DataFrame([[affiliation['affiliation-name'],affiliation['city'],affiliation['country'],affiliation['aff_id']]],columns=affiliations.columns)
        affiliations=affiliations.append(affil).drop_duplicates()   
        print(affiliations)
        affiliations.to_csv('affiliations.csv',index=False,sep='\t')    
    except :
        pass
    

   
   
