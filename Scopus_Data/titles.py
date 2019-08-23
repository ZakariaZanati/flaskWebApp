import pyscopus
from pyscopus import Scopus
import pandas as pd


key='bc87ef89794f6f531edb4162d12d3e7e'
scopus = Scopus(key)
authors = pd.read_csv("authors.csv")

authors_id=authors['author_id'].values

publications=pd.DataFrame(columns=['title', 'cover_date','authors'])


for i in range(210,len(authors_id)):
        try:
                author_publications_df=scopus.search_author_publication(authors_id[i],count=500)
                author_publications_df=author_publications_df[['title', 'cover_date','authors']]
                publications=publications.append(author_publications_df)
                print(publications)
                publications.to_csv('titles.csv',index=False,sep='\t')
                print(i+1) 
        except :
                pass
    
