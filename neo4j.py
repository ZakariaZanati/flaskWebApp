from py2neo import Graph , Node , Relationship

graph = Graph()


#systemctl start neo4j.service

def create_author(author_name , author_id , affiliation_id = None):

    author = author_name = Node("Author" , name = author_name , id = author_id , affiliation_id = affiliation_id)
    graph.create(author_name)


def create_affiliation(affiliation_name , aff_id , city = None , country = None):

    affiliation = affiliation_name = Node("Affiliation" , name = affiliation_name , city = city , country = country , id = aff_id)
    graph.create(affiliation_name)

def create_publication(title , cover_date ,	authors_id = []):

    publication =  title = Node("Publication" , title = title , date = cover_date , authors_id = authors_id )
    graph.create(title)

