import neo4j
import pandas as pd
import ast
import re, datetime



authors = pd.read_csv("Scopus_Data/authors.csv")


for author in authors.values:
    neo4j.create_author(author[1],str(author[0]),author[2]) 


affiliations=pd.read_csv("Scopus_Data/affiliations.csv", sep='\t')

for affiliation in affiliations.values:
    neo4j.create_affiliation(affiliation[0],affiliation[3],affiliation[1],affiliation[2])




publications = pd.read_csv("Scopus_Data/titles.csv",'\t')

for publication in publications.values:
    try:
        match = re.search('\d{4}', publication[1])
        date = datetime.datetime.strptime(match.group(), '%Y').date()
        neo4j.create_publication(publication[0],date.year,ast.literal_eval(publication[2]))

    except :
        pass
    





   

